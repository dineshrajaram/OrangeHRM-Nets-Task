*** Settings ***
Library    SeleniumLibrary
Library    json
Library    OperatingSystem
Library    Collections
Documentation    Contains keywords that support the framework such as setup, teardown and test data related keywords.
*** Variables ***
${test_data_file_path}    ${CURDIR}${/}..${/}test_data${/}
${test_data_file_name}    test_data.json
*** Keywords ***

Get Headless options
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --headless 
    call Method    ${options}    add_argument    --disable-dev-shm-usage
    Call Method    ${options}    add_argument    --disable-gpu
    [Return]    ${options}

Load Test Data
    [Documentation]    loads the test data from the test data file(json).
    ...    Loaded data is set as a test variable with name {test_data} and is accessible anywhere with in the scope of the test
    [Arguments]    ${scenario}
    ${text_content}    Get File    ${test_data_file_path}${test_data_file_name}
    ${data}    Loads    ${text_content}
    Dictionary Should Contain Key    ${data}    ${scenario}    Test for the given scenario not available.
    Set Test Variable    ${test_data}    ${data}[${scenario}]

Get Executable Path
    [Arguments]    ${browser}
    IF    ${{$browser.lower()=='chrome'}}
        Import Library    webdriver_manager.chrome.ChromeDriverManager
        ${path}    webdriver_manager.chrome.ChromeDriverManager.Install
    ELSE IF    ${{$browser.lower()=='firefox'}}
        Import Library    webdriver_manager.firefox.GeckoDriverManager
        ${path}    webdriver_manager.firefox.GeckoDriverManager.Install
    ELSE IF    ${{$browser.lower()=='edge'}}
        Import Library    webdriver_manager.microsoft.EdgeChromiumDriverManager
        ${path}    webdriver_manager.microsoft.EdgeChromiumDriverManager.Install
    ELSE
        Import Library    webdriver_manager.chrome.ChromeDriverManager
        ${path}    webdriver_manager.chrome.ChromeDriverManager.Install
    END
    [Return]    ${path}