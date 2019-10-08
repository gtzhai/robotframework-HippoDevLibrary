*** Settings ***
Documentation     示波器系统功能相关，如语言，时间，蜂鸣器等
Library           HippoDevLibrary
*** Variables ***
*** Keywords ***
获取按键音开启状态
  [arguments]     ${dev}
  ${ret}    beeper_status   ${dev}
  Return_From_Keyword     ${ret}

