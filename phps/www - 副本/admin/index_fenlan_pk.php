<?php
/*
 * Created on 2018-1-30
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */


?>


		<div>
			<div class="row">

				<div class="col-md-3">
					<?php
function fenlan($sql){



$my_mysql = new M_mysql();

$result = $my_mysql->select($sql);

return $result;

	}

function show_fen ($result) {

	if ($result->num_rows >0) {
//输出数据
while ($row = $result->fetch_assoc()) {

    echo "<a href=?fenlan_pk={$row['id']}> <p>{$row['name']}({$row['heji']})</p> </a>";

}
$result->close();
}
else{

	echo "没得数据?";
	$result->close();
}

}




$fenlan_sql= <<<EOF
SELECT
	fenlei. NAME as `name`,
	COUNT(fenlei.id) as heji,
	fenlei.id as id
FROM
	blog_wenzhang_fenlei AS fenlei
JOIN blog_wenzhang_neirong AS neirong ON fenlei.id = neirong.wenzhang_fenlei_id_id
WHERE
	neirong.daohanglan_id_id = 15
GROUP BY
	fenlei.`name`
EOF;




$result_fenlan = fenlan($fenlan_sql);

show_fen($result_fenlan);


?>




				</div>

				<div class="col-md-9">

					<div style="padding-bottom:10px">
<?php
$show_neirongs = <<<EOF
SELECT
	neirong.id,
	fenlei. NAME AS fenlei_name,
	neirong.biaoti as title,
	neirong.wenzhang_neirongs as neirong
FROM
	blog_wenzhang_fenlei AS fenlei
JOIN blog_wenzhang_neirong AS neirong ON fenlei.id = neirong.wenzhang_fenlei_id_id
WHERE
	neirong.daohanglan_id_id = 15  and fenlei.id={$_GET['fenlan_pk']}

EOF;


function show_neirong ($result) {

	if ($result->num_rows >0) {
//输出数据
while ($row = $result->fetch_assoc()) {

    echo "<b>{$row['fenlei_name']}</b>";
    echo "<a href=/wenzhang_chaxun.php?pk={$row['id']}> {$row['title']}</a>";
    echo "<hr>";

}
$result->close();
}
else{

	echo "没得数据?";
	$result->close();
}


}

$result_neirongs = fenlan($show_neirongs);

show_neirong($result_neirongs);



	//<b ></b>

		//






?>



						   </div>





				</div>


			</div>


		</div>


