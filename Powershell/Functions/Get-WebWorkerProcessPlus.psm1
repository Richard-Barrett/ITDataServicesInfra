function Get-WebWorkerProcessPlus
{
    [CmdletBinding()]
    param ( [switch]$Format )

    function Format-HumanReadable($size) 
    {
        switch ($size) 
        {
            {$_ -ge 1PB}{"{0:#.#'P'}" -f ($size / 1PB); break}
            {$_ -ge 1TB}{"{0:#.#'T'}" -f ($size / 1TB); break}
            {$_ -ge 1GB}{"{0:#.#'G'}" -f ($size / 1GB); break}
            {$_ -ge 1MB}{"{0:#.#'M'}" -f ($size / 1MB); break}
            {$_ -ge 1KB}{"{0:#'K'}" -f ($size / 1KB); break}
            default {"{0}" -f ($size) + "B"}
        }
    }
    
    function Get-IISVersion($osver)
    {
        switch -regex ($osver)
        {
            '^(?=.*?\b2012\b)(?=.*?\bR2\b).*$' { $iisver = '8.5' }
            '^(?=.*?\b2012\b)((?!R2).)*$' { $iisver = '8.0' }
            '^(?=.*?\b2008\b)(?=.*?\bR2\b).*$' { $iisver = '7.5' }
            '^(?=.*?\b2008\b)((?!R2).)*$' { $iisver = '7.0' }
            default { $iisver = 'unknown' }
        }
        return $iisver
    }

    function Get-AppPoolName($cmdline) 
    {
        [regex]$pattern="-ap ""(.+)"""
        $pmatch = $pattern.Match($cmdline).Groups[1].Value
        $pmatch.Substring(0, $pmatch.IndexOf(""""))
    }

    try 
    {
        $wmiq = 'SELECT * FROM Win32_Process WHERE Name = "w3wp.exe"'
        $wps = Get-WmiObject -Query $wmiq -ErrorAction Stop

        if ($wps)
        {
            [void][Reflection.Assembly]::LoadWithPartialName("Microsoft.Web.Administration")
            $iis = New-Object -TypeName Microsoft.Web.Administration.ServerManager

            if ($Format)
            {
                foreach ($wp in $wps)
                {                 
                    $apname = Get-AppPoolName $wp.CommandLine
                    $ap = $iis.ApplicationPools["$apname"]
                    $wp | Select-Object @{n='Computer';e={$_.CSName}}, 
                        @{n='PID';e={$_.ProcessId}},
                        @{n='AppPoolName';e={$apname}},
                        @{n='AppPoolID';e={$ap.ProcessModel.IdentityType}},
                        @{n='AppPoolMode';e={$ap.ManagedPipelineMode}},
                        @{n='MRVer';e={$ap.ManagedRuntimeVersion}},
                        @{n='WS';e={Format-HumanReadable $_.WorkingSetSize}},
                        @{n='PM';e={Format-HumanReadable $_.PrivatePageCount}},
                        @{n='VM';e={Format-HumanReadable $_.VirtualSize}},
                        @{n='IISVer';e={Get-IISVersion $_.OSName}}
                }
            }
            else 
            {
                foreach ($wp in $wps)
                {
                    $apname = Get-AppPoolName $wp.CommandLine
                    $ap = $iis.ApplicationPools["$apname"]
                    
                    $wppattr = New-Object System.Collections.Specialized.OrderedDictionary
                    $wppattr.Add('Computer',$wp.CSName)
                    $wppattr.Add('PID',$wp.ProcessId)
                    $wppattr.Add('AppPoolName',$apname)
                    $wppattr.Add('AppPoolID',$ap.ProcessModel.IdentityType)
                    $wppattr.Add('AppPoolMode',$ap.ManagedPipelineMode)
                    $wppattr.Add('RuntimeVer',$ap.ManagedRuntimeVersion)
                    $wppattr.Add('WorkingSet',$wp.WorkingSetSize)
                    $wppattr.Add('Private',$wp.PrivatePageCount)
                    $wppattr.Add('Virtual',$wp.VirtualSize)
                    $wppattr.Add('IISVer',(Get-IISVersion $wp.OSName))
                            
                    $wppobj = New-Object -TypeName PSObject -Property $wppattr
                    $wppobj.PSObject.TypeNames.Insert(0,'BinaryNature.W3WPPlus')
                            
                    Write-Output $wppobj    
                }
            }
        }
    }
    catch
    {
        $err = $_.Exception.Message
        Write-Warning "$env:COMPUTERNAME - $err"
    }
}
