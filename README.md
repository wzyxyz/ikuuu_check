# ikuuu机场签到<br/>
## 作用
>每天进行签到，获取额外的流量奖励

## 推送方式
根据ikuuu发布页，搜寻ikuuu可用地址，并且自动签到，该脚本采用的是<a href = 'https://sct.ftqq.com/'>Server酱</a>的推送方式，如果不需要推送，就下面的SCKEY参数的值设置为<b>空</b>就行

# 部署过程
 
1. 右上角Fork此仓库
2. 然后到`Settings`→`Secrets and variables`→`Actions` 新建以下参数：

| 参数   | 是否必须  | 内容  | 
| ------------ | ------------ | ------------ |
| EMAIL  | 是  | 账号邮箱  |
| PASSWD | 是  | 账号密码  |
| SCKEY  | 否  | Sever酱秘钥  |
<br/>

3. 到`Actions`中创建一个workflow，运行一次，以后每天项目都会自动运行。<br/>
4. 最后，可以到Run sign查看签到情况，同时也会也会将签到详情推送到Sever酱。
