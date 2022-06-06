# OrangeHRM-Nets-Task
Project created to implement the requested test automation framework for Nets.

Follow the below steps to execute the tests. Requested task has been implemented using two frameworks.

1. using robotframework + selenium 
2. using pytest + selenium 


**Setup Environment to exeucte tests.**

    1.  Install Python (recommended version - 3.10 as this was the version used for development)
    2.  clone the repository
    3. Navigate to the cloned repository in the terminal
    4. execute the below command to install all dependencies to execute the tests.
        pip install -r requirements.txt

**Execute robotframework tests**

    1. Execute the below command
        robot -A ./robotframework/resources/config/robotoptions.args .

**Execute pytest tests**

    1. Sitch to the pytest directory by executing the below command 
        cd pytest_selenium_framework
    2. Execute the tests using the below command
            pytest
        OR if you need a specific browser then 
            pytest --browser chrome
        OR
            pytest --browser edge

**Allure Report**

    Allure integration is available in both pytest and robotframework implementations.
    Allure report folder will be found under the respective results folder after execution.
    Navigate to the respective allure report folder in terminal and enter the below command to open the allure report
        allure serve
    Note : Allure should be installed seperately on the machine. requirements.txt only installs the necessary integration.
