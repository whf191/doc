<?php
header("content-type:text/html;charset=gbk");
/*
 * Created on 2018-2-3
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
 include "M_mysql.php";
?>

<?php


if (array_key_exists("pk",$_POST)) {

	$pk = $_POST['pk'];

	$sql_cj_type = "SELECT b1.id,C.name from (SELECT A.id,A.type_chengji_id_id from baishi_chengjibiao as A " .
			"  WHERE A.xuesheng_id_id={$pk}) as b1
JOIN baishi_type_chengji C ON b1.type_chengji_id_id = C.id
ORDER BY b1.id DESC";

            $my = new  M_mysql();
   			$result= $my->select($sql_cj_type);
   			$shuchu ="";
			if ($result->num_rows > 0) {

				while ($row = $result->fetch_assoc()) {

				$shuchu .="<p><button type='button' class='btn btn-primary' id='chengji_bt1'  onclick='cj_chaxun({$row['id']})'>{$row['name']}</button></p>";

  }
  echo $shuchu;
$result->close();
}
else{

	echo "没有绑定学生";
	$result->close();
}





}


?>
