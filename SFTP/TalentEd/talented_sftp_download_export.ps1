param (
    Get-Content .\files.txt | Select-String "localPath"
    Get-Content .\files.txt | Select-String "remotePath"
)
 
try
{
    # Load WinSCP .NET assembly
    Add-Type -Path "C:\Program Files (x86)\WinSCP\WinSCPnet.dll"
 
    # Setup session options
    $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
        Get-Content .\secrets.txt | select-string "Protocol"
        Get-Content .\secrets.txt | select-string "HostName"
        Get-Content .\secrets.txt | select-string "UserName"
        Get-Content .\secrets.txt | select-string "Password"
        Get-Content .\secrets.txt | select-string "SshHostKeyFingerprint"
    }
 
    $session = New-Object WinSCP.Session
 
    try
    {
        # Connect
        $session.Open($sessionOptions)
 
        # Upload files
        $transferOptions = New-Object WinSCP.TransferOptions
        $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary
 
        $transferResult =
            $session.GetFiles($remotePath, $localPath, $False, $transferOptions)
 
        # Throw on any error
        $transferResult.Check()
 
        # Print results
        foreach ($transfer in $transferResult.Transfers)
        {
            Write-Host "Download of $($transfer.FileName) succeeded"
        }
    }
    finally
    {
        # Disconnect, clean up
        $session.Dispose()
    }
 
    exit 0
}
catch
{
    Write-Host "Error: $($_.Exception.Message)"
    exit 1
}

