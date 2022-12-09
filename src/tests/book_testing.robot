*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***

Page is Open
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open

Register A Book
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open
    Set Identifier  maija
    Set Author  kalle
    Set Editor  kalle
    Set Title  kalle
    Set Publisher  kalle
    Set Year  2002
    Submit Credentials
    Page Should Contain  maija

Get Bibtex Format
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open
    Click Button  Muuta bibtex-muotoon
    Bibtex Page Should Be Open

Register A Book With A Wrong Year
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open
    Set Identifier  okokok
    Set Author  kalle
    Set Editor  kalle
    Set Title  kalle
    Set Publisher  kalle
    Set Year  232040
    Submit Credentials
    Registering A Book Should Fail With Message  Lisää julkaisuvuosi.

Delete Oldest Registered Book
    Main Page Should Be Open
    Click Link  Kirja
    Book Page Should Be Open
    Click Button  Poista viite
    Page Should Not Contain  maija


*** Keywords ***


Registering A Book Should Fail With Message
    [Arguments]  ${message}
    Book Page Should Be Open
    Page Should Contain  ${message}

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