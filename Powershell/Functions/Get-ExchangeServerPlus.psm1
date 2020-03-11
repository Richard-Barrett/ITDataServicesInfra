function Get-ExchangeServerPlus
{
<#
Get-ExchangeServerPlus
Written By Paul Flaherty, http://blogs.flaphead.com
Modified by Jeff Guillet, http://www.expta.com
Modified by Mark E. Smith, http://marksmith.netrends.com
Modified by Jason Sherry, http://blog.jasonsherry.net | Version 2.0
Modified yet again by Marc Weisel, http://binarynature.blogspot.com
Let's just label it [v3.0] - 04/24/2013
#>    
    [CmdletBinding()]
    param 
    (
        [Parameter(ValueFromPipeline=$true,
                   ValueFromPipelineByPropertyName=$true)]
        [Alias('hostname')]
        [Alias('cn')]
        [string]$ComputerName
    )
    
    BEGIN
    {
        # Set registry prefix path variables
        $regprod = "SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products"
        $reguninst = "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\"
        # Get a list of EXCH servers
        if ($ComputerName)
        {
            $exchservers = Get-ExchangeServer -Identity $ComputerName -ErrorAction Stop | 
            Where-Object { $_.IsEdgeServer -eq $false }
        }
        else
        {
            $exchservers = Get-ExchangeServer | Where-Object { $_.IsEdgeServer -eq $false }
        }
    }

    PROCESS 
    {
        foreach ($exchserver in $exchservers)
        {
            try
            {
                # Get OS info (version and service pack)
                $os = Get-WmiObject -ComputerName $exchserver.Name `
                      -Class Win32_OperatingSystem -ErrorAction Stop
                $osversion = $os.Caption
                $svcpack = $os.ServicePackMajorVersion
                
                # Get architecture type (32 or 64 bit)
                if ($osversion -like '*2003*')
                {
                    $cs = Get-WmiObject -ComputerName $exchserver.Name `
                          -Class Win32_ComputerSystem -ErrorAction Stop
                    $numbits = $cs.SystemType
                }
                else { $numbits = $os.OSArchitecture }
            }
            catch
            {
                # Check for common DCOM errors and display "friendly" output
                switch ($_)
                {
                    { $_.Exception.ErrorCode -eq 0x800706ba } `
                        { $err = 'Unavailable (Host Offline or Firewall)'; 
                            break; }
                    { $_.CategoryInfo.Reason -eq 'UnauthorizedAccessException' } `
                        { $err = 'Access denied (Check User Permissions)'; 
                            break; }
                    default { $err = $_.Exception.Message }
                }
                Write-Warning "$($exchserver.Name) - $err"
            }

            # Get Build Number (Version)
            $major = ($exchserver.AdminDisplayVersion).major
            $minor = ($exchserver.AdminDisplayVersion).minor
            $build = ($exchserver.AdminDisplayVersion).build
            $revision = ($exchserver.AdminDisplayVersion).revision
            [Version]$exchbuildnum = "$major.$minor.$build.$revision" 
        
            # Get EXCH Roles
            $whichroles = @()
            if ($exchserver.ServerRole -like '*Mailbox*') { $whichroles += 'MB' }
            if ($exchserver.ServerRole -like '*Hub*') { $whichroles += 'HT' }
            if ($exchserver.ServerRole -like '*Client*') { $whichroles += 'CAS' }
            if ($exchserver.ServerRole -like '*Unified*') { $whichroles += 'UM' }
            $roles = [System.String]::Join(',', $whichroles)
            
            # Set registry path for each EXCH version and populate version attribute 
            if ($exchserver.IsExchange2007OrLater)
            {
                if ($exchserver.IsE14OrLater) 
                {
                    if ($exchserver.AdminDisplayVersion -like 'Version 14.*') 
                    {
                        $key = "$regprod\AE1D439464EB1B8488741FFA028E291C\Patches\"
                        $exchver = '2010'
                    }
                    else 
                    { 
                        $key = "$reguninst\Microsoft Exchange v15\"
                        $altkey = "$reguninst\{4934D1EA-BE46-48B1-8847-F1AF20E892C1}\"
                        $exchver = '2013'
                    }
                }
                else 
                {
                    $key = "$regprod\461C2B4266EDEF444B864AD6D9E5B613\Patches\"
                    $exchver = '2007'
                }
            }
            else { Write-Warning "Exchange server version could not be determined." }
            
            try 
            {
                if ($key)
                {
                    # Connect to the server's remote registry and 
                    # query for update data
                    $srv = $exchserver.Name
                    $type = [Microsoft.Win32.RegistryHive]::LocalMachine
                    $regkey = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey($type, $srv)
                    $regkey = $regkey.OpenSubKey($key)
                    $updates = @()
                    # Query registry for EXCH 2007 and 2010 servers
                    if ($exchver -match '^20[0|1][7|0]$')
                    {
                        foreach($sub in $regkey.GetSubKeyNames())
                        {
                            $subkey = $key + $sub
                            $subregkey = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey($type, $srv)
                            $subregkey = $subregkey.OpenSubKey($subkey)
                        
                            foreach($subx in $subregkey.GetValueNames())
                            {
                                # Get installed date and displayname properties of the EXCH patch
                                if ($subx -eq 'Installed')   
                                {
                                    $instdate = $subregkey.GetValue($subx)
                                    $instdate = $instdate.substring(4,2) + "/" + `
                                    $instdate.substring(6,2) + "/" + $instdate.substring(0,4)
                                }
                                if ($subx -eq 'DisplayName') 
                                {
                                    $updval = $subregkey.GetValue($subx)
                                    $ur = $updval.SubString($updval.LastIndexOf(' ') + 1)
                                    $desc = $updval.Substring(0,$updval.LastIndexOf($ur) - 1)
                                }
                            }
                            # Create object for update rollup info
                            $updobj = New-Object -TypeName PSObject -Property @{
                                InstallDate=$instdate
                                UpdateBuild=[Version]$ur
                                Description=$desc
                            }
                            $updates += $updobj
                            # Close connection
                            $subregkey.Close()
                        }
                    }
                    # Query registry for EXCH 2013 servers
                    else
                    {
                        $altregkey = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey($type, $srv)
                        $altregkey = $altregkey.OpenSubKey($altkey)
                        foreach ($keyprop in $regkey.GetValueNames())
                        {
                            if ($keyprop -eq 'DisplayName')
                            {
                                $desc = $regkey.GetValue($keyprop)
                            }
                        }
                        foreach ($altkeyprop in $altregkey.GetValueNames())
                        {
                            if ($altkeyprop -eq 'InstallDate')
                            {
                                $instdate = $altregkey.GetValue($altkeyprop)
                                $instdate = $instdate.substring(4,2) + "/" + `
                                $instdate.substring(6,2) + "/" + $instdate.substring(0,4)
                            }
                            if ($altkeyprop -eq 'DisplayVersion')
                            {
                                $cu = $altregkey.GetValue($altkeyprop)
                            }
                        }
                        # Create PSObject for cumulative update info
                        $updobj = New-Object -TypeName PSObject -Property @{
                            InstallDate=$instdate
                            UpdateBuild=[Version]$cu
                            Description=$desc
                        }
                        $updates += $updobj
                        # Close connection
                        $altregkey.Close()
                    }
                    # Close connection
                    $regkey.Close()
                }
                else 
                { 
                    Write-Warning "Could not retrieve update data for $($exchserver.Name)." 
                }
            }
            catch 
            {
                $err = $_.Exception.Message
                Write-Warning "$($exchserver.Name) - $err"
            }
            
            # Create (and populate) an ordered dictionary collection with
            # Exchange Server Plus object properties for cleaner default output (PS3 or later)
            $exchprops = New-Object System.Collections.Specialized.OrderedDictionary
            $exchprops.Add("Name",$exchserver.Name)
            $exchprops.Add("Version",$exchver)
            $exchprops.Add("Edition",$exchserver.Edition)
            $exchprops.Add("Build",$exchbuildnum)
            $exchprops.Add("Update",$updates)
            $exchprops.Add("Role",$roles)
            $exchprops.Add("OSVer",$osversion)
            $exchprops.Add("OSSP",$svcpack)
            $exchprops.Add("OSArch",$numbits)
            
            # Create Exchange Server Plus object
            $exchsrvplus = New-Object -TypeName PSObject -Property $exchprops
            $exchsrvplus.PSObject.TypeNames.Insert(0,'BinaryNature.ExchangeServerPlus')
            Write-Output $exchsrvplus
        }
    }
}
