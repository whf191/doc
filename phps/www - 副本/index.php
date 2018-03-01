<?php
header("content-type:text/html;charset=gbk");
?>

<?php
//引入自定义库

include "index_head.php";
include "M_mysql.php";
include "index_welcome.php";

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

      <div class="jumbotron">
              <?php
welcome();
              ?>
      </div>

     <?php
    if (array_key_exists('fenlan_pk',$_GET)) {

		include "index_fenlan_pk.php";


	}
	else {
		include "index_content.php";
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
