*** Settings ***
Library           HippoDevLibrary
Library           Dialogs
*** Variables ***
*** Keywords ***
提示操作员
    [arguments]     ${msg}
    pause_execution    ${msg}
