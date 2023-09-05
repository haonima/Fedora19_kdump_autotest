# 简介

Fedora19_kdump_autotest是一款针对Fedora 19 Kdump的自动化测试套件，可以支持在Fedora 19上面对Kdump的自动化测试。

# 安装使用

1. 进入目录后，使用命令`python setup.py`进行安装。安装位置为`/usr/local/ftest`
2. 安装后，需要进入`/usr/local/ftest/ftest.conf.d/ftest.conf`进行配置，选择系统crash方式、vmlinux位置以及kdump选项。
3. 在分析crash得到的vmcore文件时，可以自定义crash命令。这些命令需要写入`/usr/local/ftest/ftest.conf.d/cmds.conf`
4. 配置完成之后，运行命令`ftest`开始测试。最后得到的结果会放在`/usr/local/ftest/results`目录下
5. 测试完成后可以修改配置文件进行下一轮测试。但在开始下一轮测试前需要运行命令`ftest clear`进行初始化。
6. 每次测试后会覆盖掉前一次测试得到的结果，所以进行测试时请确认已经保存好之前的结果。


# 注意事项

1. 如果需要串口输出，则需要在安装之前设置串口，具体方式为在启动参数之后加
`console=ttyS1,115200k`
2. 在需要sshdump的时候，请事先配好ssh的authorized_keys，使无需输入密码即可登录
3. 串口输出参数请在envpara.py文件中的SERIAL参数配置
4. 在使用nfs dump的时候需要安装nfs-utils包



# 接下来的工作

添加自定义串口、重写输出类，将所有输出重新写到串口及log，完成本地的存储方式（local，包括raw和本地）
