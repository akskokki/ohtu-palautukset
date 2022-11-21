*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Succeed

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username too short

Login After Failed Registration
    Go To Login Page
    Set Username  k
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  ville1
    Set Password Confirmation  ville1
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville456
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}