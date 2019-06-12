                                        **~~解客科技ICEM系统接口自动化框架~~**


一：基于Python + unittest + requests 接口自动化框架

    python版本python3.7.3
    
二：代码结构

    common文件夹下存放一些公共的方法和一些固定的参数
    mysqlHandle文件夹下存放操作数据库相关的代码
    Report文件夹用于存放测试报告
    sendEmail文件夹存放发送邮件及报告附件的方法
    test_interface文件夹下存放业务接口，接口自动化框架代码存放处
    testData用于存放测试数据，测试用例
    HTMLTestRunner为html格式的报告模板
    run_test.py文件为自动化的入口文件
    
三：run_test.py参数介绍
    
    项目参数：根据需要可筛选不同的业务模块测试用例来执行，目前支持"CPD"，"MA","SETUP"
    环境参数：开发人员可选择开发环境来执行接口自动化，测试人员可以选择测试环境来执行，目前支持"dev","qa"
    
四：执行run_test.py

    执行python run_test.py "项目参数" "环境参数"  就可执行自动化程序
    例如：python run_test.py MA qa
    例如：python run_test.py CDP qa
    例如：python run_test.py SETUP dev
    