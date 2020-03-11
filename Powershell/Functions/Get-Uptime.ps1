function Get-Uptime
{
    [CmdletBinding()]
    param
    (
        [Parameter(ValueFromPipeline=$true,
                   ValueFromPipelineByPropertyName=$true)]
        [Alias('hostname')]
        [Alias('cn')]
        [string[]]$ComputerName = $env:COMPUTERNAME
    )

    BEGIN {}

    PROCESS
    {
        foreach ($computer in $ComputerName)
        {
            try
            {
                $os = Get-WmiObject -Class Win32_OperatingSystem `
                -ComputerName $computer -ErrorAction Stop
                $time = $os.ConvertToDateTime($os.LocalDateTime) - `
                        $os.ConvertToDateTime($os.LastBootUpTime)

                # Create property hash table for custom PS object 
                $props = @{'Computer'=$os.CSName;
                           'Days'=$time.Days;
                           'Hours'=$time.Hours;
                           'Minutes'=$time.Minutes;
                           'Seconds'=$time.Seconds;}

                # Create custom PS object and apply type
                $uptime = New-Object -TypeName PSObject -Property $props
                $uptime.PSObject.TypeNames.Insert(0,'BN.Uptime')

                Write-Output $uptime
            }
            catch
            {
                # Check for common DCOM errors and display "friendly" output
                switch ($_)
                {
                    { $_.Exception.ErrorCode -eq 0x800706ba } `
                        { $err = 'Unavailable (Host Offline or Firewall)' }
                    { $_.CategoryInfo.Reason -eq 'UnauthorizedAccessException' } `
                        { $err = 'Access denied (Check User Permissions)' }
                    default { $err = $_.Exception.Message }
                }
                Write-Warning "$computer - $err"
            }
        }
    }

    END {}

}
