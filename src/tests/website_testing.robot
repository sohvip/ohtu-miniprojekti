*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***

Page is Open
    Main Page Should Be Open
    Click Link  Lisää nettisivu
    Website Page Should Be Open

Register A Website
    Main Page Should Be Open
    Click Link  Lisää nettisivu
    Website Page Should Be Open
	Set Identifier  kalle
	Set Title  kalle
	Set Editor  kalle
	Set How_published  https://github.com/sohvip/ohtu-miniprojekti
	Set Year  2003
	Set Note  20.12.2012
    Submit Credentials
    Registering A Website Should Succeed


*** Keywords ***

Registering A Website Should Succeed
    Website Page Should Be Open

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

