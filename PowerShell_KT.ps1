#Frederik Kruusimäe
#01.02.2023
#Powershell KT



$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

$fail = Import-csv $dir/MOCK_DATA.csv | Select-Object ip_address -skip 1
new-item $dir\ip.txt

foreach($ip in $fail){
    $terveip = $ip.ip_address
    $osa = $terveip.Split(".")
    $uusip = ""
    foreach($iposa in $osa)
    {
        $iposa = [int]$iposa
        if ($iposa -ge 0 -and $iposa -le 255){
            $uusip += [string]$iposa+"."
        }  
        elseif ($iposa -lt 0 -or $iposa -gt 255)
        {
            $uusip = ""
            break
        }
    }
    if ($uusip -ne ""){
        $uusip = $uusip.TrimEnd(".")
        $uusip >> $dir\ip.txt
    }
}
