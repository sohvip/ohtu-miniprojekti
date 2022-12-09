*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Etusivu

Go To Main Page
    Go To  ${HOME URL}

Website Page Should Be Open
    Title Should Be  Nettisivun lisääminen

Bibtex Page Should Be Open
    Title Should Be  BibTeX-muoto
