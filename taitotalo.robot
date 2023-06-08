Run Suite|Debug Suite| Load in Interactive Console
*** Settings ***
Library    RPA.Browser.Selenium
Library    RPA.Desktop

Documentation    kadjfmoåkdfmdåpasfmdsåflpsdomfpsldfm,s

Load in Interactive Console
*** Variables ***
${NETTIOSOITE}    www.taitotalo.fi
${SELAIN}    firefox
${HAKUSANA}    Python
${KUVANNIMI}    kuva.png

*** Keywords ***
Load in Interactive Console
Avaa taitotalon sivu
    Open Available Browser    www.taitotalo.fi


Load in Interactive Console
Hae hakukentässä
    Input Text    hakusanat    Python
    Click Button    edit-submit-search-results

Load in Interactive Console
Ota kuvakaappaus
    Take Screenshot    kuva.png


Load in Interactive Console
Sulje Selain
    Close Browser    ${NETTIOSOITE}    ${}


*** Tasks ***

*** Test Cases ***
Run|Debug|Run in Interactive Console
Testaa Taitotalon haku
    Avaa taitotalon sivu
    Hylkää evästeet
    Hae hakukentässä
    Ota kuvakaappaus

*** Comments ***