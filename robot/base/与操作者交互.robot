*** Settings ***
Library           HippoDevLibrary
Library           Dialogs
*** Variables ***
*** Keywords ***
提示操作员
    [arguments]     ${msg}
    pause_execution    ${msg}

打印到控制台
    [arguments]     ${msg}
    log_to_console      ${msg}

