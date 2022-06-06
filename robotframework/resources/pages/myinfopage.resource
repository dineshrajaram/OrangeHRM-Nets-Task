*** Settings ***
Library    SeleniumLibrary


*** Keywords ***

Get Full Name
    [Documentation]    Returns the full name of the user mentioned above the profile picture
    ${element_fullname_xpath}    Set Variable    //div[@id="profile-pic"]/h1
    Page Should Contain Element    ${element_fullname_xpath}
    ${full_name}    Get Text    ${element_fullname_xpath}
    [Return]    ${full_name}