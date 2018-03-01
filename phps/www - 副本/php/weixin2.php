<?php
/*
 * Created on 2018-1-30
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
 //http://qydev.weixin.qq.com/wiki/index.php?title=%E4%B8%BB%E5%8A%A8%E8%B0%83%E7%94%A8 ÀÏÎÄµµ

?>
<?php
$url1="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx512775916d2936ff&corpsecret=qFU2CKPJpo4sGj2BYBx3IoHApKnemmdhrhbK5578rPc";
$WEIXIN_USRE_URL = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=r_2D7NIMQmTwo0PuF-IUEPbvRFmTdwBQnCLoo663x-_ATS_us7PcCjkL59LU0oGqBOesK2A2uY2HeX-Iswzy2P62PHnYzoyIjvhqUQzW9i5Uhn_qC4DuCTqjecYlpjywyotH-Y4OQVbmLTB2vHtFbHtHVo4NThk0SBQZJePDYkivjctwucAjRJeXbQD9kt75C4CRXkJBeWUiUoUNFokK0Q&code=';
$code = $_GET('code');
$WEIXIN_USRE_URL .=$code;


$curl = curl_init();

curl_setopt($curl, CURLOPT_URL, $WEIXIN_USRE_URL);
curl_setopt($curl, CURLOPT_HEADER, 1);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, true);
$data = curl_exec($curl);
curl_close($curl);

echo $data;

?>

<?php



?>
