#coding=utf-8
from  __future__ import  unicode_literals
def qpm(pk):

    queding_peizhi_moban = """  <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#qpmmyModal%s">
	配置保存
</button>
<!-- 模态框（Modal） -->
<div class="modal fade" id="qpmmyModal%s" 
"""  % (pk,pk)

    queding_peizhi_moban2 = """
tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
 aria-hidden="true" data-keyboard="false" data-backdrop="static">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
			<!-- 
				<button type="button" class="close" data-dismiss="modal" aria-hidden="false">
					&times;
				</button>
				 -->
				<h4 class="modal-title" id="myModalLabel">
					配置保存
				</h4>
			</div>"""
    queding_peizhi_moban3 =   """
			<div class="modal-body">
				<p id="qpmresult%s">等待修改...</p>
			</div>
			<div class="modal-footer">""" % pk


    queding_peizhi_moban4 = """
				<button id="qpmguanbi%s" type="button" class="btn btn-default" data-dismiss="modal">关闭
				</button>
				<!-- 
				<button type="button" class="btn btn-primary">
					提交更改
				</button>
				-->
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal -->

<script>

$('#qpmmyModal%s').on('show.bs.modal', function () {

        function qpmchange%s(id=%s){
         
        qpmpost_change%s(id);

        };

  

  qpmchange%s();
  });
   """ % (pk,pk,pk,pk,pk,pk)
    queding_peizhi_moban6 = """

function qpmpost_change%s(pk){
	//隐藏发版按钮...
	 $("#qpmguanbi").attr('disabled','');
    $.ajax({url:'/is_container_config/',error:function(xhr){
         $("#qpmresult%s").html("")
         $("#qpmresult%s").append("错误提示:" + xhr.status + "" + xhr.statusText);
         $("#qpmguanbi%s").removeAttr("disabled");

   },     type:'POST',data:{pk:pk},
   success:function(data,textStatus){
      $("#qpmresult%s").html("")
      $("#qpmresult%s").append("完成提示:" + data );
	 
      $("#qpmguanbi%s").removeAttr("disabled");
        qpmguanbi_moban%s();
   }

   });

	
	
};


function qpmguanbi_moban%s(){
    //点关闭后，刷新
     $('#qpmmyModal%s').on('hide.bs.modal',
    function() {
        window.location.reload();
    })
    
   }




</script>



"""  % (pk,pk,pk,pk,pk,pk,pk,pk,pk,pk)

    return queding_peizhi_moban + queding_peizhi_moban2 +queding_peizhi_moban3 +queding_peizhi_moban4  +queding_peizhi_moban6

def qcc(pk,pk_time,container_name,container_host,container_port,container_script):

    queding_container_create = """  <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#newmyModal%s">
	创建容器
</button>
<!-- 模态框（Modal） -->
<div class="modal fade" id="newmyModal%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
 aria-hidden="true" data-keyboard="false" data-backdrop="static">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
			<!-- 
				<button type="button" class="close" data-dismiss="modal" aria-hidden="false">
					&times;
				</button>
				 -->
				<h4 class="modal-title" id="myModalLabel">
					创建容器
				</h4>
			</div>
			<div class="modal-body">
				<h4 id="new1result%s"  style="color:red" ></h4>
				<h4>确定参数无误，点击提交按钮.</h4>
				<hr>
				<p>容器名称   : %s</p>
				<p>容器宿主机: %s</p>
				<p>开放的端口: %s</p>
				<p>绑定的脚本: %s</p>

			</div>
			<div class="modal-footer">
				<button id="new1guanbi%s" type="button" class="btn btn-default" data-dismiss="modal">关闭
				</button>

				<button id="newtijiao%s"  type="button" class="btn btn-primary">
					提交
				</button>

			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal -->
"""  % (pk_time,pk_time,pk_time,container_name,container_host,container_port,container_script,pk_time,pk_time)
    queding_container_create1 = """
<script>

$('#newmyModal%s').on('show.bs.modal', function () {
             $("#new1result%s").html("")
  });








$('#newtijiao%s').click(function(){
        
      post_change%s(pk=%s);

  });

function post_change%s(pk){
	//隐藏发版按钮...
	 $("#new1guanbi%s").attr('disabled','');
    $.ajax({url:'/is_container_create/',error:function(xhr){
         $("#new1result%s").html("")
         $("#new1result%s").append("错误提示:" + xhr.status + "" + xhr.statusText);
         $("#new1guanbi%s").removeAttr("disabled");

   },     type:'POST',data:{pk:pk},
   success:function(data,textStatus){
      $("#new1result%s").html("")
      $("#new1result%s").append("完成提示:" + data );

      $("#new1guanbi%s").removeAttr("disabled");
        guanbi_moban();
   }

   });



};


function guanbi_moban%s(){

     $('#newmyModal%s').on('hide.bs.modal',
    function() {
        window.location.reload();
    })

   }




</script>



"""  % (pk_time,pk_time,pk_time,pk_time,pk,pk_time,pk_time,pk_time,pk_time,pk_time,pk_time,pk_time,pk_time,pk_time,pk_time)
    return queding_container_create + queding_container_create1

def ccs(pk):
    change_container_script = """  <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal%s">
	修改脚本
</button>
<!-- 模态框（Modal） -->
<div class="modal fade" id="myModal%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
 aria-hidden="true" data-keyboard="false" data-backdrop="static">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
			<!-- 
				<button type="button" class="close" data-dismiss="modal" aria-hidden="false">
					&times;
				</button>
				 -->
				<h4 class="modal-title" id="myModalLabel">
					修改脚本
				</h4>
			</div>
			<div class="modal-body">
				<h4 id="result%s"  style="color:red" ></h4>
				<h4>确定无误，点击提交按钮.</h4>
				<hr>


<div class="div1">
<textarea id="mylove%s"></textarea>
</div>
"""  % (pk,pk,pk,pk)

    change_container_script1 = """

            <!--   end -->

			</div>
			<div class="modal-footer">
				<button id="guanbi%s" type="button" class="btn btn-default" data-dismiss="modal">关闭
				</button>

				<button id="sc_tijiao%s"  type="button" class="btn btn-primary">
					提交
				</button>

			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal -->
     """ % (pk,pk)

    change_container_script2 = """
<script>

$('#myModal%s').on('show.bs.modal', function () {
        $("#result%s").html("");
        $("#mylove%s").html("");
        $("#mylove%s").css("width","100%%").css("height","300");

           get_script%s(pk=%s); 

  });

function get_script%s(pk){
    window.script_id=pk;
    $.ajax({url:"/get_contalner_script/",error:function(xhr){
         $("#result%s").html("");
         $("#result%s").append("错误提示:" + xhr.status + "" + xhr.statusText);


   },     type:'POST',data:{pk:pk},
   success:function(data,textStatus){
      //$("#result").html("");
     //alert(data);
      $("#mylove%s").val(data);

   }});
};

$('#sc_tijiao%s').click(function(){

      post_script_change%s(pk=window.script_id);

  });

function post_script_change%s(pk){
	 $("#guanbi%s").attr('disabled','');

    $.ajax({url:'/get_contalner_script/',error:function(xhr){
         $("#result%s").html("")
         $("#result%s").append("错误提示:" + xhr.status + "" + xhr.statusText);
         $("#guanbi%s").removeAttr("disabled");

   },     type:'POST',data:{pk:pk,sc_val:$("#mylove%s").val()},
   success:function(data,textStatus){
      $("#result%s").html("")
      $("#result%s").append("完成提示:" + data );

      $("#guanbi%s").removeAttr("disabled");

   }

   });



};

</script>

""" % (pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk)
    return change_container_script + change_container_script1 + change_container_script2

def remote_exec_script(pk):
    remote_exec_container_script = """  <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#execmyModal%s">
    	调用脚本
    </button>
    <!-- 模态框（Modal） -->
    <div class="modal fade" id="execmyModal%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
     aria-hidden="true" data-keyboard="false" data-backdrop="static">
    	<div class="modal-dialog">
    		<div class="modal-content">
    			<div class="modal-header">
    			<!-- 
    				<button type="button" class="close" data-dismiss="modal" aria-hidden="false">
    					&times;
    				</button>
    				 -->
    				<h4 class="modal-title" id="myModalLabel">
    					执行脚本
    				</h4>
    			</div>
    			<div class="modal-body">
    				<h4 id="execresult%s"  style="color:red" ></h4>
    				
    				<hr>


    <div class="div1">
    <p id="execmylove%s"></p>
    </div>
    """ % (pk, pk, pk, pk)

    remote_exec_container_script1 = """

                <!--   end -->

    			</div>
    			<div class="modal-footer">
    				<button id="execguanbi%s" type="button" class="btn btn-default" data-dismiss="modal">关闭
    				</button>
                    <!--
    				<button id="execsc_tijiao%s"  type="button" class="btn btn-primary">
    					提交
    				</button>
    				-->
    				<button id="execstart%s"  type="button" class="btn btn-primary">
    					start
    				</button>
    				<button id="execrestart%s"  type="button" class="btn btn-primary">
    					restart
    				</button>
    				<button id="execstop%s"  type="button" class="btn btn-primary">
    					stop
    				</button>

    			</div>
    		</div><!-- /.modal-content -->
    	</div><!-- /.modal -->
         """ % (pk, pk,pk,pk,pk)

    remote_exec_container_script2 = """
    <script>
    //公共锁按钮
    function lock_buttion(){
     $("#execguanbi%s").attr('disabled','');
     $("#execstart%s").attr('disabled','');
     $("#execrestart%s").attr('disabled','');
     $("#execstop%s").attr('disabled','');
    
    };
    //公共释放按钮
        function release_buttion(){
     $("#execguanbi%s").removeAttr('disabled','');
     $("#execstart%s").removeAttr('disabled','');
     $("#execrestart%s").removeAttr('disabled','');
     $("#execstop%s").removeAttr('disabled','');
    
    };
    
    //写个公共的调用函数
        function exectiaoyong_script%s(state){
        var pk = window.script_id;
        $.ajax({url:"/remote_call_script/",error:function(xhr){
            lock_buttion();
             $("#execresult%s").html("");
             $("#execmylove%s").append("远程调用此容器脚本失败，调用状态:" + state  + "-->");
             $("#execmylove%s").append("错误提示:" + xhr.status + "" + xhr.statusText + "<br><hr>");
            release_buttion();

       },     type:'POST',data:{pk:pk,state:state},
       success:function(data,textStatus){
          //$("#execresult").html("");
         //alert(data);
            lock_buttion();
          $("#execmylove%s").append(data);
          release_buttion();
 
       }});
    };
     
    $('#execstart%s').click(function(){
           exectiaoyong_script%s(state='start');
    
    
    });
    
        $('#execrestart%s').click(function(){
           
    exectiaoyong_script%s(state='restart');
    
    });
    
        $('#execstop%s').click(function(){
           exectiaoyong_script%s(state='stop');
    
    
    });
    

    $('#execmyModal%s').on('show.bs.modal', function () {
            $("#execresult%s").html("");
            $("#execmylove%s").html("");
            $("#execmylove%s").css("width","100%%").css("height","300");

               execget_script%s(pk=%s); 

      });

    function execget_script%s(pk){
        window.script_id=pk;
        $.ajax({url:"/remote_exec_script/",error:function(xhr){
             $("#execresult%s").html("");
             $("#execmylove%s").append("远程获取此容器开放的端口失败-->");
             $("#execmylove%s").append("错误提示:" + xhr.status + "" + xhr.statusText + "<hr>");
             

       },     type:'POST',data:{pk:pk},
       success:function(data,textStatus){
          //$("#execresult").html("");
         //alert(data);
          $("#execmylove%s").val(data);

       }});
    };

    $('#execsc_tijiao%s').click(function(){

          execpost_script_change%s(pk=window.script_id);

      });

    function execpost_script_change%s(pk){
    	 $("#execguanbi%s").attr('disabled','');

        $.ajax({url:'/remote_exec_container_script/',error:function(xhr){
             $("#execresult%s").html("")
             $("#execresult%s").append("错误提示:" + xhr.status + "" + xhr.statusText);
             $("#execguanbi%s").removeAttr("disabled");

       },     type:'POST',data:{pk:pk,sc_val:$("#mylove%s").val()},
       success:function(data,textStatus){
          $("#execresult%s").html("")
          $("#execresult%s").append("完成提示:" + data );

          $("#execguanbi%s").removeAttr("disabled");

       }

       });

    };

    </script>

    """ % (pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk, pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk,pk)
    return remote_exec_container_script + remote_exec_container_script1 + remote_exec_container_script2
