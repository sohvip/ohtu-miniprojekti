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
    Set Identifier  w700
    Set Author  Collins Allan
    Set Editor  Ann Holum
    Set Title  Clean Code: A Handbook of Agile Software Craftmanship
    Set Publisher  Prentice Hall
    Set Year  2008
    Submit Credentials
    Page Should Contain  Collins Allan

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
    Set Identifier  b708
    Set Author  Austen Jane
    Set Editor  Juva Kersti
    Set Title  Ylpeys ja ennakkoluulo
    Set Publisher  WSOY
    Set Year  232040
    Submit Credentials
    Registering A Book Should Fail With Message  Lisää julkaisuvuosi.

Delete Oldest Registered Book
    Main Page Should Be Open
    Click Link  Kirja
    Book Page Should Be Open
    Click Button  Poista viite
    Page Should Not Contain  Collins Allan

Add A Tagged Book
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open
    Set Identifier  e606
    Set Author  Hawking Stephen
    Set Editor  Murray John
    Set Title  Brief Answers to the Big Questions
    Set Publisher  Bantam Books
    Set Year  2018
    Submit Credentials
    Page Should Contain  Hawking Stephen
    Set Tag_text  tietotekniikka
    Click Button  Lisää tägi

Find A Tagged Book
    Main Page Should Be Open
    Click Button  Kirja
    Book Page Should Be Open
    Set Identifier  s476
    Set Author  Jansson Tove
    Set Editor  Heilala Katariina
    Set Title  Muumilaakson kertomuksia
    Set Publisher  Tammi
    Set Year  2019
    Submit Credentials
    Page Should Contain  Jansson Tove
    Set Tag_text  lastenkirja
    Click Button  Lisää tägi  
    Click Link  Takaisin
    Main Page Should Be Open
	Set Citation_identifier  lastenkirja
    Click Button  Etsi
    Tag Page Should Be Open

    


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

Set Tag_text
    [Arguments]  ${tag_text}
    Input Text  tag_text  ${tag_text}

Set Citation_identifier
    [Arguments]  ${citation_identifier}
    Input Text  citation_identifier  ${citation_identifier}