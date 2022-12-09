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
	Set Identifier  mikko
	Set Title  kalle
	Set Editor  kalle
	Set How_published  https://github.com/sohvip/ohtu-miniprojekti
	Set Year  2003
	Set Note  20.12.2012
    Submit Credentials
    Page Should Contain  mikko

Register A Website With Wrong URL
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  miisa
	Set Title  kalle
	Set Editor  kalle
	Set How_published  j
	Set Year  2002
	Set Note  20.12.2012
    Submit Credentials
    Registering A Website Should Fail With Message  Lisää URL.

Register A Website With Wrong Year
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
	Set Identifier  maija
	Set Title  kalle
	Set Editor  kalle
	Set How_published  https://github.com/sohvip/ohtu-miniprojekti
	Set Year  202223
	Set Note  20.12.2012
    Submit Credentials
    Registering A Website Should Fail With Message  Tarkista julkaisuvuosi.

Delete Oldest Registered Book
    Main Page Should Be Open
    Click Link  Nettisivu
    Website Page Should Be Open
    Click Button  Poista viite
    Page Should Not Contain  mikko

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

