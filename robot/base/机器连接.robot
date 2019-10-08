*** Settings ***
Documentation     实现连接和断开机器的操作
Library           HippoDevLibrary
*** Variables ***
*** Keywords ***
连接机器
    [arguments]     ${dev}      ${name}=default
    session_connect     ${dev}      ${name}
    get_idn     ${dev}

断开机器
    [arguments]     ${dev}
    session_disconnect      ${dev}

注册机器
    [arguments]     ${dev}
    register_specical_dev       ${dev}

卸载机器
    [arguments]     ${dev}
    unregister_specical_dev       ${dev}

清场
    session_reset_all
