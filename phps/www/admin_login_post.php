<?php
session_start();
header("content-type:text/html;charset=gbk");
/*
 * Created on 2018-1-31
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
?>

<?php

	if (array_key_exists("username",$_POST) and array_key_exists("password",$_POST)) {

$username=trim($_POST['username']);
$password=trim($_POST['password']);

if ($username == "wan") {
	if ($password == "pass"){

		//echo "��¼�ɹ�,����session";
		//���ٵ�ǰseesion
		//unset($_SESSION['username']);
		$_SESSION['username']=array($username,'13683457200');
		header("location:/index.php");

	}else {
		echo "�������";
	}
}
else {
	echo "�û�������";
}





	}

	else {
		echo "��������";
	}







?>

