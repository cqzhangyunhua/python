

环境：conda activate python3.10
参考： pyppeteer  https://www.cnblogs.com/ruhai/p/11134639.html

清华源

-i https://pypi.tuna.tsinghua.edu.cn/simple

阿里源

-i https://mirrors.aliyun.com/pypi/simple

中科大源

-i https://pypi.mirrors.ustc.edu.cn/simple/


-----------流程方式------------------

1.后台分配帐号
1.1子帐号登录可以添加url
1.2添加任务，选择url， 设置跑的数量 ，设置跑的时间段，发布任务  (ip与app的调用方法)


key  ip1_app1

ip1===>app1
ip1===>app2
ip1===>app3
ip1===>app4


ip1===>app1
ip2===>app1
ip3===>app1
ip4===>app1




redis列队

验证技术 任务机X取redis是不同和任务

1.任务机
  跑完成一条回写服务器表记录

任务机1 取redis 列队
任务机2 取redis 列队
任务机3 取redis 列队


买流量 ->订单表
用户  ip数(数量与金额)    订单号(规则任意) 金额 时间,是否支付，支付时间
付款记表
用户 订单号 金额 时间

微信，支付宝配置
