*** Settings ***
Library    SeleniumLibrary
Library    String
Documentation    Conatins all keywords / actions that can be performed on the home page of the website.
*** Keywords ***

Navigate to Tab
    [Documentation]    navigates to the specified tab. tab name is case sensitive and should ne exactly the same as seen on the screen.
    [Arguments]    ${tab_name}
    ${tab_elem_xpath}    Set Variable    //ul[@id="mainMenuFirstLevelUnorderedList"]/li[a/b[text()="${tab_name}"]]
    Page Should Contain Element    ${tab_elem_xpath}    Tab with text ${tab_name} not found.
    Click Element    ${tab_elem_xpath}
    ${selected_tab_class}    Get Element Attribute    ${tab_elem_xpath}    class
    Should Start With    ${selected_tab_class}    current
    
Get Loggedin User name
    [Documentation]    Rerturn the name of the loggedin user
    Page Should Contain Element    id:welcome    Welcome Message Not found. User may not be logged in.
    ${text}     Get Text    id:welcome
    ${username}    Remove String    ${text}    Welcome${SPACE}    
    [Return]    ${username}   

Logout
    Page Should Contain Element    id:welcome    Welcome Message Not found. User may not be logged in.
    Click Element    id:welcome
    ${visible_welcome_dropdown}    Set Variable    //div[@id="welcome-menu" and contains(@style,"block")]
    Page Should Contain Element    ${visible_welcome_dropdown}        Welcome menu was not expanded.
    Wait Until Page Contains Element    ${visible_welcome_dropdown}//li/a[text()="Logout"]
    Wait Until Keyword Succeeds    30 sec    3 sec    Click Element    ${visible_welcome_dropdown}//li/a[text()="Logout"]
    Wait Until Location Contains    login
    Page Should Contain Element    id:txtUsername