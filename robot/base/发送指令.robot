*** Settings ***
Library           HippoDevLibrary
*** Variables ***
*** Keywords ***
发送询问指令
    [arguments]     ${dev}      ${cmds}
    ${ret}      query       ${dev}       ${cmds}
    Return_From_Keyword     ${ret}

发送控制指令
    [arguments]     ${dev}      ${cmds}
    write   ${dev}       ${cmds}
