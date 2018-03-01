<?php
header("content-type:text/html;charset=gbk");
/*
 * Created on 2018-1-31
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
 include "../M_mysql.php";
date_default_timezone_set("PRC");
$riqi=date ( "Y-m-d H:i:s" );
?>


<?php





if ($_SERVER['REQUEST_METHOD']  == "POST" ) {
	$my_mysql = new M_mysql("utf-8");

	if ($_GET['t'] == "change") {

$neirong_id = $_POST['neirong_id'];
$name =  $_POST['name'];
$editor1 = $_POST['editor1'];
$editor1 = addslashes($editor1);
$sql = "update blog_wenzhang_neirong set wenzhang_neirongs='{$editor1}' , biaoti='{$name}' where id='{$neirong_id}' ";


if ($my_mysql->update($sql)) {
 echo "change is ok";
}
else {
	echo "not is ok";
}

	}
	else {

		$fl_pk = $_POST['pk'];
	$name =  $_POST['name'];
	$editor1 = $_POST['editor1'];

$sql =  " INSERT INTO blog_wenzhang_neirong
(`changjian_shijian`, `biaoti`, `wenzhang_neirongs`, `daohanglan_id_id`,
`tubian2_id`, `wenzhang_fenlei_id_id`) VALUES ('{$riqi}', '{$name}' , '{$editor1}','15', '7', '{$fl_pk}')" ;



if ($my_mysql->into($sql)) {
	echo "ok...";
}
else {
	echo "not ok ...";
}

	}

$my_mysql->colse();


}

else {
	die("不是post".$_SERVER['REQUEST_METHOD']);
}



?>