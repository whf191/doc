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

	$sql_cj_type = "SELECT
	t.yuwen,
	t.shuxue,
	t.yingyu,
	t.zhengzhi,
	t.lishi,
	t.dili,
	t.shengwu,t.wuli
FROM
	baishi_chengjibiao t
WHERE
	t.id = '{$pk}'";

            $my = new  M_mysql();
   			$result= $my->select($sql_cj_type);
   			$shuchu ="";
   			$hanzi = array("yuwen"=>"����","shuxue"=>"��ѧ",
   			"yingyu"=>"Ӣ��",
   			"zhengzhi"=>"����",
   			"lishi"=>"��ʷ",
   			"dili"=>"����",
   			"shengwu"=>"����",
   			"wuli"=>"����",
   			);
			$zongfen=0;
			if ($result->num_rows > 0) {

				while ($row = $result->fetch_assoc()) {
					$row_key = array_keys($row);
                    for ($index = 0; $index < sizeof($row_key); $index++) {
                    	$key = $row_key[$index];
                    	$key2 = $hanzi[$key];
                    	if ($row[$key]) {
                           $shuchu .= "{$key2}:{$row[$key]} ";
                           $zongfen +=$row[$key];
						}


					}


  }
  echo $shuchu . " " . "�ֺܷϼ�:{$zongfen}";
$result->close();
}
else{

	echo "û�а�ѧ��";
	$result->close();
}





}


?>
