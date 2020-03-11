function Get-DiskUsage ([string]$path=".") {
    $groupedList = Get-ChildItem -Recurse -File $path | Group-Object directoryName | select name,@{name='length'; expression={($_.group | Measure-Object -sum length).sum } }
    foreach ($dn in $groupedList) {
        New-Object psobject -Property @{ directoryName=$dn.name; length=($groupedList | where { $_.name -like "$($dn.name)*" } | Measure-Object -Sum length).sum }
    }
}
