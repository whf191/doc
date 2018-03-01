<?php

include_once "WXBizMsgCrypt.php";

// 假设企业号在公众平台上设置的参数如下
$encodingAesKey = "8GZj827ZBwiQTFUocnpfoUg4yOXWFqtMd5Dg5Jfbf2k";
$token = "zS6qGnGFX9M67yfAlWsxrx1OV";
$corpId = "wx512775916d2936ff";

//设置utf-8应该是最最最关键的一步
//header("Content-Type:text/html; charset=utf-8");

/*
------------使用示例一：验证回调URL---------------
*企业开启回调模式时，企业号会向验证url发送一个get请求
假设点击验证时，企业收到类似请求：
* GET /cgi-bin/wxpush?msg_signature=5c45ff5e21c57e6ad56bac8758b79b1d9ac89fd3×tamp=1409659589&nonce=263014780&echostr=P9nAzCzyDtyTWESHep1vC5X9xho%2FqYX3Zpb4yKa9SKld1DsH3Iyt3tP3zNdtp%2B4RPcs8TgAE7OaBO%2BFZXvnaqQ%3D%3D
* HTTP/1.1 Host: qy.weixin.qq.com

接收到该请求时，企业应
1.解析出Get请求的参数，包括消息体签名(msg_signature)，时间戳(timestamp)，随机数字串(nonce)以及公众平台推送过来的随机加密字符串(echostr),
这一步注意作URL解码。
2.验证消息体签名的正确性
3. 解密出echostr原文，将原文当作Get请求的response，返回给公众平台
第2，3步可以用公众平台提供的库函数VerifyURL来实现。

*/

//$sVerifyMsgSig = HttpUtils.ParseUrl("msg_signature");
//$sVerifyMsgSig = "5c45ff5e21c57e6ad56bac8758b79b1d9ac89fd3";
//$sVerifyTimeStamp = HttpUtils.ParseUrl("timestamp");
//$sVerifyTimeStamp = "1409659589";
//$sVerifyNonce = HttpUtils.ParseUrl("nonce");
//$sVerifyNonce = "263014780";
//$sVerifyEchoStr = HttpUtils.ParseUrl("echostr");
//$sVerifyEchoStr = "P9nAzCzyDtyTWESHep1vC5X9xho/qYX3Zpb4yKa9SKld1DsH3Iyt3tP3zNdtp+4RPcs8TgAE7OaBO+FZXvnaqQ==";
// $sVerifyMsgSig = HttpUtils.ParseUrl("msg_signature");



$sVerifyMsgSig = $_GET['msg_signature'];
// $sVerifyTimeStamp = HttpUtils.ParseUrl("timestamp");
$sVerifyTimeStamp = $_GET['timestamp'];
// $sVerifyNonce = HttpUtils.ParseUrl("nonce");
$sVerifyNonce = $_GET['nonce'];
// $sVerifyEchoStr = HttpUtils.ParseUrl("echostr");
$sVerifyEchoStr = $_GET['echostr'];
// 需要返回的明文
// 需要返回的明文，官方给出的，实际没用的参数，最终输出是$sEchoStr
//header('content-type:text');//以及这个地方配置内容的格式
$EchoStr = "";
//$sVerifyMsgSig = urldecode($sVerifyMsgSig);
//$sVerifyTimeStamp = urldecode($sVerifyTimeStamp);
//$sVerifyNonce = urldecode($sVerifyNonce);
//$sVerifyEchoStr = urldecode($sVerifyEchoStr);
$wxcpt = new WXBizMsgCrypt($token, $encodingAesKey, $corpId);
$errCode = $wxcpt->VerifyURL($sVerifyMsgSig, $sVerifyTimeStamp, $sVerifyNonce, $sVerifyEchoStr, $sEchoStr);
if ($errCode == 0) {
    //header('content-type:text');
    //
    // 验证URL成功，将sEchoStr返回
    // HttpUtils.SetResponce($sEchoStr);
    echo $EchoStr;
} else {
    print("ERR: " . $errCode . "\n\n");
}