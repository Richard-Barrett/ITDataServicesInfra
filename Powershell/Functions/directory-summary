function directory-summary($dir=".") { 
  get-childitem $dir | 
    % { $f = $_ ; 
        get-childitem -r $_.FullName | 
           measure-object -property length -sum | 
             select @{Name="Name";Expression={$f}},Sum}
}
