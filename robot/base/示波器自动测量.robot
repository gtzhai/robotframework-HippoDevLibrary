*** Settings ***
Documentation     实现示波器自动测量相关操作
Library           HippoDevLibrary
*** Variables ***
*** Keywords ***
打开测量
    [Documentation]     参数dev：要操作的机器的visa地址
    [arguments]     ${dev}
    measure_on      ${dev}

获取通道一双峰值
    [arguments]     ${dev}
    ${val}    measure_vpp    ${dev}     CHANnel1
    Return_From_Keyword     ${val}

获取通道二双峰值
    [arguments]     ${dev}
    ${val}    measure_vpp    ${dev}     CHANnel2
    Return_From_Keyword     ${val}

获取通道三双峰值
    [arguments]     ${dev}
    ${val}    measure_vpp    ${dev}     CHANnel3
    Return_From_Keyword     ${val}

获取通道四双峰值
    [arguments]     ${dev}
    ${val}    measure_vpp    ${dev}     CHANnel4
    Return_From_Keyword     ${val}

关闭测量
    [arguments]     ${dev}
    measure_off     ${dev}

