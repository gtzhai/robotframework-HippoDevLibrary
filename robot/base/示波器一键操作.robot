*** Settings ***
Documentation     示波器一键操作功能，如autoset等
Library           HippoDevLibrary
*** Variables ***
*** Keywords ***
自动设置示波器
  [arguments]     ${dev}
  autoset       ${dev}
