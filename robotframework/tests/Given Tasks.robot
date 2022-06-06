*** Settings ***
Resource    ../resources/pages/loginpage.resource
Resource    ../resources/pages/homepage.resource
Resource    ../resources/pages/myinfopage.resource

# step 1.a and 2.a  Navigate to the test site in a browser
Suite Setup        Launch Application
Suite Teardown    Close All Browsers
*** Test Cases ***
Scenario 1 - invalid credentials
    [Documentation]    login with invalid credentials and verified the error message.
    ...    test data is loaded from flat file (json)
    [Setup]    Load Test Data    Scenario 1
    #1.b login with random user name and password. Data is read from json formatted test data file.
    Login into application    ${test_data}[username]    ${test_data}[password]
    #1.c validate invalid credentials message
    Validate Invalid Login message

Scenario 2 - Extract Credentials and Login
    [Documentation]    Extracts the username and password from the login page and logs in with the extracted credentials and checks for the username.
    #2.b capture username and password mentioned in the test screen
    ${username}    ${password}    Get Username and Password from Page
    #2.c use then and log in
    Login into application    ${username}    ${password}
    # additional step to validate successful login
    Validate Successful Login
    #2.d validate that upon successful login, you are able to see the logged in user.
    ${user}    Get Loggedin User name
    #2.e print the name of the user in the report. Setting log level to warn so it can be seen at the top of the report
    Log    Logged in User Name is : ${user}    WARN
    [Teardown]    Logout

Additional Scenario - Get Full Name from Info Tab
    [Documentation]    Navigates to the My info tab and get the full name of the user
    ${username}    ${password}    Get Username and Password from Page
    Login into application    ${username}    ${password}
    Validate Successful Login
    Navigate to Tab    My Info
    ${full_name}    Get Full Name
    Log    Full Name of the user is : ${full_name}    WARN
    [Teardown]    Logout 