<?php
header("content-type:text/html;charset=gbk");
/*
 * Created on 2018-1-31
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

?>

<script src="/static/ckeditor/ckeditor.js"></script>
<?php

$change_id = "";
$change_biaoti="";
$change_neirong = "";
$change_fenlan_id = "";


if (array_key_exists("change",$_GET) and array_key_exists("admin_fenlan_add_pk",$_GET) and array_key_exists("pk",$_GET) ) {
	$change=$_GET['change'];
	$pk_fenlan = $_GET['admin_fenlan_add_pk'];
	$pk_neirong = $_GET['pk'];
	$my_mysql = new M_mysql();
    $sql = "select t.id,t.biaoti,t.wenzhang_neirongs,t.wenzhang_fenlei_id_id from blog_wenzhang_neirong t where t.id={$pk_neirong}" .
    		" and t.wenzhang_fenlei_id_id={$pk_fenlan}";

	$result = $my_mysql->select($sql);
	if ($result->num_rows >0 ) {
		while ($row = $result->fetch_assoc()){
			$change_id = $row['id'];
			$change_biaoti=$row['biaoti'];
			$change_neirong = $row['wenzhang_neirongs'];
			$change_fenlan_id = $row['wenzhang_fenlei_id_id'];

		}
	}




}



if (array_key_exists("admin_fenlan_add_pk",$_GET)) {
   //ҵ���߼�����

 //echo "pk ���� �� {$_GET['admin_fenlan_add_pk']}";
	$pk_fenlan = $_GET['admin_fenlan_add_pk'];
}
else {

 echo "pk ������..";

}



?>

    <form  action="/admin/admin_fenlan_add_post.php" method="post"  id="bd1">


                      	<div class="form-group">
         <label for="name">pk</label>
		<input type="text" class="form-control"   id="pk" value=<?php echo $pk_fenlan ?> readonly
			   placeholder="����������"   name="pk">
		<label for="name">����</label>
		<input type="text" class="form-control"   id="name"
			   placeholder="����������"   name="zhuti" value= <?php echo $change_biaoti ?> >
	</div>
        <label for="name">����</label>
        <textarea name="editor1" id="editor1" rows="10" cols="80">
        			<?php  if ($change_neirong) {
						 echo $change_neirong;
					}
					else {
					  echo 	"д��ʲô��";
					}
					 ?>

            </textarea>
            <script>
                // Replace the <textarea id="editor1"> with a CKEditor
                // instance, using default configuration.
                CKEDITOR.replace( 'editor1' );
            </script>


        </form>
        <?php
	if ($change) {
	echo "<button  onclick='change_dianwo({$change_id})' id='fabiao_bt1'>�޸�</button>";
	}
else {
	echo "<button  onclick='dianwo()' id='fabiao_bt1'>����</button>";
}

         ?>

<script>
    function dianwo(){
        var gy_content=CKEDITOR.instances.editor1.getData();
        var gy_name = $("#name").val();
        var pk = $("#pk").val();

      //���ط���ť...
	 $("#fabiao_bt1").attr('disabled','');

      $.ajax({url:'/admin/admin_fenlan_add_post.php?t=ajax',error:function(xhr){
         alert("����ʧ�ܴ�����ʾ:" + xhr.status + "" + xhr.statusText);
         $("#fabiao_bt1").removeAttr("disabled");

   },    type:'POST',data:{name:gy_name,editor1:gy_content,pk:pk},
                            success:function(data,textStatus){
                                           $("#fabiao_bt1").removeAttr("disabled");
                                                    var rs_data = data;
                                                    alert(rs_data);
//                                                    var arr_data = rs_data.split("|");
//                                                    if (arr_data[0]  == 0) {
//                                                              window.location.href = arr_data[1];
//                                                    }
//                                                    else{
//                                                                    alert("����ʧ��:--->" +  arr_data[1] );
//
//                                                    };




   }

   });



    };
</script>

<script>
    function change_dianwo(neirong_id){
        var gy_content=CKEDITOR.instances.editor1.getData();
        var gy_name = $("#name").val();
        var pk = $("#pk").val();
        var neirong_id = neirong_id;

      //���ط���ť...
	 $("#fabiao_bt1").attr('disabled','');

      $.ajax({url:'/admin/admin_fenlan_add_post.php?t=change',error:function(xhr){
         alert("����ʧ�ܴ�����ʾ:" + xhr.status + "" + xhr.statusText);
         $("#fabiao_bt1").removeAttr("disabled");

   },    type:'POST',data:{name:gy_name,editor1:gy_content,neirong_id:neirong_id},
                            success:function(data,textStatus){
                                           $("#fabiao_bt1").removeAttr("disabled");
                                                    var rs_data = data;
                                                    console.log(rs_data);
//                                                    var arr_data = rs_data.split("|");
//                                                    if (arr_data[0]  == 0) {
//                                                              window.location.href = arr_data[1];
//                                                    }
//                                                    else{
//                                                                    alert("����ʧ��:--->" +  arr_data[1] );
//
//                                                    };




   }

   });



    };
</script>
