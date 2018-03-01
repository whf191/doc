<?php
/*
 * Created on 2018-1-30
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

?>


<?php

function welcome(){

$my_sql = new M_mysql();

$gerenhuan_sql = <<<EOF
SELECT
	blog_geren_huanying_lan.`name`
FROM
	blog_geren_huanying_lan
WHERE
	blog_geren_huanying_lan.daohanglan_id_id = 15

EOF;

$gerenhuan_sql_result = $my_sql->select($gerenhuan_sql);

if ($gerenhuan_sql_result->num_rows >0) {
//输出数据
while ($row = $gerenhuan_sql_result->fetch_assoc()) {

    echo " <p>{$row['name']}</p>";

}

$gerenhuan_sql_result->close();
}
else{

	echo "没得数据?";
	$gerenhuan_sql_result->close();
}

}




?>