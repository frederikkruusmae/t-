cls

$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath


$xml = [xml](Get-Content $dir\customers.xml)

$rows = $xml.customers.customer

ForEach($row in $rows){
    if( $row.country -eq "Bolivia"){
        $row.full_name}}