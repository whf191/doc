<?php
header("content-type:text/html;charset=gbk");
?>

<?php
//引入自定义库

include "../index_head.php";
include "../M_mysql.php";


?>


<!DOCTYPE html>
<html lang="zh-CN">
  <head>

    <meta charset="UTF-8">
    <title><?php  echo $blogname; ?></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Loading Bootstrap -->
    <link href="/static/dist/css/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Loading Flat UI -->
    <link href="/static/dist/css/flat-ui.css" rel="stylesheet">

  </head>
  <body>
    <style>
      body {
        min-height: 100%;

      }

      code {
    padding: 2px 6px;
    font-size: 85%;
    color: #333;
    background-color: #f9f2f4;
    border-radius: 4px;
}


      .navbar-static-top {
        margin-bottom: 19px;
      }
    </style>

    <!-- Static navbar -->
    <div class="navbar navbar-default navbar-static-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
          </button>
          <a class="navbar-brand" href="/"><?php  echo $blogname; ?></a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
					<?php
					for ($index = 0; $index < sizeof($daohao); $index++) {

    					echo "<li ><a href='{$daohao[$index][0]}'>{$daohao[$index][1]}</a> </li>";
					}
            ?>



          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#"><?php echo $houtaiguanli ?></a></li>


          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


    <div class="container">

      <!-- Main component for a primary marketing message or call to action -->

<?php
    if (array_key_exists('pk',$_GET)) {

		$pk=$_GET['pk'];
		$pk_mysql =  new M_mysql();
$pk_chaxun_sql = <<<EOF
SELECT
	t.biaoti AS title,
	t.wenzhang_neirongs AS neirong
FROM
	blog_wenzhang_neirong t
WHERE
	t.id = {$pk}
EOF;


		$pk_result = $pk_mysql->select($pk_chaxun_sql);

		if ($pk_result->num_rows >0) {
			while ($row = $pk_result->fetch_assoc()) {
				echo "<h6>{$row['title']}</h6>";
				echo "<hr>";
				echo "<p>{$row['neirong']}</p>";
			}

		}









	}
	else {
		die("没有数据");
	}




?>






    </div> <!-- /container -->

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="/static/dist/js/vendor/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/static/dist/js/flat-ui.min.js"></script>

    <script src="/static/assets/js/application.js"></script>

  </body>



</html>

