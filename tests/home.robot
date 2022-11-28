*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***

Register A Book
    Set Identifier  kalle
    Set Author  kalle
    Set Editor  kalle
    Set Title  kalle
    Set Publisher  kalle
    Set Year  2002
    Submit Credentials
    Registering A Book Should Succeed

*** Keywords ***

Registering A Book Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  Tallenna kirja

Set Identifier
    [Arguments]  ${identifier}
    Input Text  identifier  ${identifier}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}