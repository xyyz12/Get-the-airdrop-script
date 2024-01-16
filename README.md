# Get-the-airdrop-script
以领取 ZKPEPE 空投，按照gm大佬的代码，写一份python代码上传

空投官网，活动已结束  https://www.zksyncpepe.com/airdrop

参考教程：https://x.com/gm365/status/1732302764641022168?s=20


1、手动 claim，查看 tx 信息(做大多数项目，第一步都会有这个)

![image](https://github.com/xyyz12/Get-the-airdrop-script/assets/91812763/ee282a12-e0e0-478d-9206-225147577f31)

可以看到 claim 交易需要两个核心参数：

 amount: 空投数量   +    proof: 证明信息
  
2、获取核心参数

搞明白 amount 和 proof  这两个参数哪来的

3、编写函数

1、获取空投数量    +    2、获取 proof   +    3、claim 函数

从浏览器的 XHR 请求中，复制对应的 CURL 命令，使用 CURL 转 Python 代码工具，即可快速搞定1和2

![image](https://github.com/xyyz12/Get-the-airdrop-script/assets/91812763/d1726d25-c3c5-4fa4-a25e-f04e33b5a014)

 CURL 转 Python 代码工具：{https://www.lddgo.net/convert/curl-to-code 、 https://www.kgtools.cn/convert/curl} 

网站的查询按钮   --》     1、获取空投数量

网站的claim按钮  --》     2、获取 proof

使用我自己编写的工具 http://wtftx.com       ，复制tx hash，即可一键转换为 claim 的 web3. py函数，这就是3、claim 函数


![image](https://github.com/xyyz12/Get-the-airdrop-script/assets/91812763/9567f9c8-03a8-41b2-8fb5-552d64ba94e9)


4、组装代码

完整的函数 = 功能函数 +  操作函数

完整的函数 = {查询空投数量、获取proof、领取空投 }  +   {增加本地读取 CSV 文件、获取私钥、循环执行} 
