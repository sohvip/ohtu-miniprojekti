*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***

Page is Open
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open

Register A Website
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  z690
	Set Title  Ohtu-miniprojekti
	Set Editor  Sohvi
	Set How_published  https://github.com/sohvip/ohtu-miniprojekti
	Set Year  2022
	Set Note  20.12.2022
    Submit Credentials
    Page Should Contain  Ohtu-miniprojekti

Get Bibtex Format
    Main Page Should Be Open
    Click Button  Nettisivu
    Website Page Should Be Open
    Click Button  Muuta bibtex-muotoon
    Website Bibtex Page Should Be Open

Register A Website With Wrong URL
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  v404
	Set Title  Ohjelmistotuotanto
	Set Editor  kalle
	Set How_published  ohjelmistotuotanto-hy.github
	Set Year  2020
	Set Note  10.12.2022
    Submit Credentials
    Registering A Website Should Fail With Message  Lisää URL.

Register A Website With Wrong Year
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  p234
	Set Title  Helsingin yliopiston nettisivut
	Set Editor  Helsingin yliopisto
	Set How_published  https://www.helsinki.fi/fi
	Set Year  202223
	Set Note  9.11.2022
    Submit Credentials
    Registering A Website Should Fail With Message  Tarkista julkaisuvuosi.

Delete Oldest Registered Website
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
    Click Button  Poista viite
    Page Should Not Contain  Ohtu-miniprojekti

Add A Tagged Book
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  z690
	Set Title  Firefox kotisivu
	Set Editor  Firefox
	Set How_published  https://www.mozilla.org/en-GB/firefox/
	Set Year  2001
	Set Note  30.10.2022
    Submit Credentials
    Page Should Contain  Firefox kotisivu
    Set Tag_text  nettisivu
    Click Button  Lisää tägi

Find A Tagged Book
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  ww909
	Set Title  Ohjelmistotuotanto viikko 3
	Set Editor  Matti Luukkainen
	Set How_published  https://ohjelmistotuotanto-hy.github.io/tehtavat3/
	Set Year  2020
	Set Note  3.12.2022
    Submit Credentials
    Page Should Contain  Ohjelmistotuotanto viikko 3
    Set Tag_text  ohjelmistotuotanto
    Click Button  Lisää tägi  
    Click Link  Takaisin
    Main Page Should Be Open
	Set Tag_text  ohjelmistotuotanto
    Click Button  Etsi
    Tag Page Should Be Open

*** Keywords ***


Registering A Website Should Fail With Message
    [Arguments]  ${message}
    Website Page Should Be Open
    Page Should Contain  ${message}


Submit Credentials
    Click Button  Tallenna sivu

Set Identifier
    [Arguments]  ${identifier}
    Input Text  identifier  ${identifier}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Set How_published
    [Arguments]  ${how_published}
    Input Text  how_published  ${how_published}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Note
    [Arguments]  ${note}
    Input Text  note  ${note}

Set Tag_text
    [Arguments]  ${tag_text}
    Input Text  tag_text  ${tag_text}

