<?php session_start(); ?>
<?php
header("content-type:text/html;charset=gbk");

/*
 * Created on 2018-2-3
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

include "M_mysql.php";
include "index_head.php";

?>

<?php


if (array_key_exists("username",$_SESSION)) {

	 $get_session  = $_SESSION['username'];



}
else {

	header("location:admin_login.php");

}
?>
<!DOCTYPE html>
<html lang="zh-CN">
   <head>
	   <meta charset="UTF-8">
      <title>�ɼ���ѯ</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- ���� Bootstrap -->
      <link href="/static/bootstrap.min.css" rel="stylesheet">

        <link rel="stylesheet" href="/static/jquery-confirm.min.css">
   </head>
   <body>
   <!--  ��������   container-fluid -->
      <div class="container">
         <div class="row">
            <div class="col-md-12">
               <nav class="navbar navbar-default" role="navigation">
	<div class="container-fluid">
	<div class="navbar-header">
		<button type="button" class="navbar-toggle" data-toggle="collapse"
				data-target="#example-navbar-collapse">
			<span class="sr-only">�л�����</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		</button>
		<a class="navbar-brand" href="#">�ɼ���ѯ</a>
	</div>
	<div class="collapse navbar-collapse" id="example-navbar-collapse">
		<ul class="nav navbar-nav">






		</ul>
	</div>
	</div>
</nav>


            </div>


            </div>

           <!--  context���� -->
         <div class="row">
            <div class="col-md-12">
            <div  id="box1" >

                <p>����λ��:�ɼ���ѯϵͳÿ��Ҫ֧���߰��ķ��������ã��������ñ�APPϵͳ�����а�����Ը�����ʦ�Ӹ��ͣ�
                    ��֧����һ�ѣ���ӭ��Ǯ���������Ŀ���������ܸ��ж���!��</p>
                <p style="text-align:left"><button type="button" class="btn btn-danger" id="zhanzhu" onclick="zhanzhu()">����˽�����������ҪС��������������Ӫ���ã�</button></p>



				    <div class="table-responsive">
	<table class="table">


		<thead>
			<tr>
				<th>�û�</th>


				<th>��ѯ</th>
			</tr>
		</thead>
		<tbody>



			<tr>

					 <td> <select id="s_sheng" class="form-control">

						  <?php
$my1 = new M_mysql();
$sql1 = "SELECT
	B.id,
	B. NAME
FROM
	baishi_jiazhang AS A
JOIN baishi_xuesheng_jiazhang_id AS C ON A.id = C.jiazhang_id
JOIN baishi_xuesheng B ON B.id = C.xuesheng_id
WHERE
	A.tel = '{$get_session[1]}'";

			$result = $my1->select($sql1);
			if ($result->num_rows > 0) {

				while ($row = $result->fetch_assoc()) {

				echo "<option  value={$row['id'] }>{$row['NAME']}</option>";

}
$result->close();
}
else{

	echo "û�а�ѧ��";
	$result->close();
}






						    ?>



                      </select>
		          </td>


				<td><button type="button" class="btn btn-danger" id="chengji_bt122" onclick="cj_chaxun2()">��ѯ</button></td>

			</tr>

		</tbody>

</table>

</div>
<div id="get_cj_types">


<div>

            </div>


         </div>




         </div>

</div>

      <script src="/static/jquery.js"></script>

      <script src="/static/bootstrap.min.js"></script>

<script src="/static/jquery-confirm.min.js"></script>
<script src="http://code.highcharts.com/highcharts.js"></script>

<script>


  function zhanzhu(){

     location.href="/zhanzhu/";

    };

  function cj_chaxun(id){

   $.ajax({url:'/fenshu_chaxun.php',error:function(xhr){
         alert("����111��ʾ:" + xhr.status + "" + xhr.statusText);


   },     type:'POST',data:{pk:id},
	  success:function(data,textStatus){
      alert("��ѯ���:  " + data );

   }

   });

 };

 function cj_chaxun2(){

    $.ajax({url:'/cj_chaxun.php',error:function(xhr){
         alert("������ʾ:" + xhr.status + "" + xhr.statusText);


   },     type:'POST',data:{pk:$('#s_sheng').val()},
	  success:function(data,textStatus){
	  $("#get_cj_types").html("");
	  $("#get_cj_types").html(data);



   }

   });

 };














  function cj_zoushi(){

     $.ajax({url:'/cj_zoushi_chaxun/',error:function(xhr){
         alert("����111��ʾ:" + xhr.status + "" + xhr.statusText);


   },     type:'POST',data:{xuesheng:$('#xuesheng').val(),kemu:$('#kemu').val()},
	  success:function(data,textStatus){
			eval( data );







	  $('#chengjizoushi').highcharts(json);

   }

   });






 };

  function cj_tongji(){

     $.ajax({url:'/cj_tongji_chaxun/',error:function(xhr){
         alert("����111��ʾ:" + xhr.status + "" + xhr.statusText);


   },     type:'POST',data:{kemu:$('#kemu').val()},
	  success:function(data,textStatus){

	    if ( data == "fail" ) {
             alert("����ɼ���ʱ��֧��ͳ�Ƴ�ͼ");
	    }
         else {
			eval( data );
			$('#chengjitongji').highcharts(json);

			};

   }

   });



 };













</script>



   </body>
</html>