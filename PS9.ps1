
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
 
$csv_header = @("email;password;nimi;kasutajanimi") 

$csv_header | Set-Content $dir\emails.csv
 
$users = Import-Csv $dir\users.csv
 
ForEach($user in $users){
    $fname = $user.first_name
    $lname = $user.last_name

    $pass = 1..3 | ForEach-Object { Get-Random -Maximum $lname.Length }
    $pass = -join $lname[$pass] 
    $pass += Get-Random -Maximum 99 -minimum 10
 
       

    $row = $fname.ToLower()+"."+$lname.ToLower()+"@metshein.com;"+$pass+";"+$fname + " " + $lname + ";" + ($fname[0] + $lname).ToLower()
   
    Add-Content $dir\emails.csv $row
    
}
