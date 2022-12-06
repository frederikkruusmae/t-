function mata
{
    <#
    .SYNOPSIS
        Esimene funktsioon arvutab ringi pindala.
    .DESCRIPTION
        See funktsioon arvutab ringi pindala etteantud raadiuse järgi.
    .EXAMPLE
        anna ringi pindala arvutamiseks raadius.
    .EXAMPLE
        Mõtle välja ringi raadius ja sisesta see, et teada saada ringi pindala.
    #>
        param($raadius)

        $s=[Math]::PI+[Math]::Pow($raadius,2)
        [Math]::Round($s,2)


}

mata(4)
Get-Help mata

function nimed
{
    $nimi = Read-Host "Mis on sinu nimi?"
    $nimi.ToTitlecase($nimi)


    $nimi
}


function matat2($nimi){
    $nimi.tolower()
    $nimi.replace("ö", "o").replace("ä", "a").replace("õ", "o").replace("ü", "u")
    (Get-Culture).TextInfo.ToTitleCase($nimi.tolower())
    
    }
    
    
matat2("õüöä")