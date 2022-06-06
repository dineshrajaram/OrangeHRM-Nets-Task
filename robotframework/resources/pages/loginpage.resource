*** Settings ***
Library    SeleniumLibrary
Library    String
Resource    ../utilities/FrameworkKeywords.resource

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/
${message}    Invalid credentials
*** Keywords ***
Launch Application
    [Documentation]    Opens the browser to the give url. sets the the browser options based on the headless argument provided.
    ...    headeless is a boolean argument. Also the sets the browser size.
    [Arguments]    ${a_url}=${url}    ${browser}=chrome    ${headless}=${False}
    IF    ${headless} and ${{$browser.lower()=='chrome'}}
        ${options}    Get Headless options
    ELSE
        ${options}    Set Variable    ${None}
    END
    ${path}    Get Executable Path    ${browser}
    Open Browser    ${a_url}    browser=${browser}    options=${options}    executable_path=${path}
    Set Window Size    1920    1080

Login into application
    [Documentation]    enters the given username and password and clicks on the Login button.
    [Arguments]    ${username}    ${password}
    Input Text    id:txtUsername    ${username}
    Input Password    id:txtPassword    ${password}
    Click Element    id:btnLogin

Validate Invalid Login message
    [Documentation]    checks for error message incase invalid login.
    ...    takes an optional argument message. if the message is not given then the default message defined in the variables section is used.
    ...    If the user provides a message then that message will be validated.
    [Arguments]    ${a_message}=${message}
    Page Should Contain Element    id:spanMessage    Page did not contain error message field.
    Element Text Should Be    id:spanMessage    ${a_message}    Error message text was not expected.  

Validate Successful Login
    [Documentation]    checks that the user is successfully logged in by checking id "dashboard" is present in the url.
    ${url_after_login}    Get Location
    Should Contain    ${url_after_login}    dashboard    URL after login did not contain "dashboard". Login might have failed.

Get Username and Password from Page
    [Documentation]    Reads the user name and password on the login page and returns them.
    ${element_xpath}    Set Variable    //span[contains(text(),"Username") and contains(text(),"Password")]
    Page Should Contain Element    ${element_xpath}    Element that contains user name and password not found.
    ${user_and_pass}    Get Text    ${element_xpath}
    @{split_text}    Split String    ${user_and_pass}    :
    ${username}    Set Variable    ${{$split_text[1].replace(' ','').split("|")[0]}}
    ${password}    Set Variable    ${{$split_text[2].replace(' ','').replace(')','')}}
    [Return]    ${username}    ${password}