#coding=utf-8
from  __future__ import  unicode_literals
def logs_download(pk):

    queding_peizhi_moban = """  <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#logsmyModal%s">
	日志下载
</button>
<!-- 模态框（Modal） -->
<div class="modal fade" id="logsmyModal%s" 
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
					日志下载
				</h4>
			</div>"""
    queding_peizhi_moban3 =   """
			<div class="modal-body">
				<p id="logsresult%s">远程拉取日志列表中...耐心等待下...</p>
			</div>
			<div class="modal-footer">""" % pk


    queding_peizhi_moban4 = """
				<button id="logsguanbi%s" type="button" class="btn btn-default" data-dismiss="modal">关闭
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

$('#logsmyModal%s').on('show.bs.modal', function () {

        function logschange%s(id=%s){
         
        logspost_change%s(id);

        };

  

  logschange%s();
  });
   """ % (pk,pk,pk,pk,pk,pk)
    queding_peizhi_moban6 = """

function logspost_change%s(pk){
	
	 $("#logsguanbi").attr('disabled','');
    $.ajax({url:'/list_online_logs/',error:function(xhr){
         $("#logsresult%s").html("")
         $("#logsresult%s").append("错误提示:" + xhr.status + "" + xhr.statusText);
         $("#logsguanbi%s").removeAttr("disabled");

   },     type:'POST',data:{pk:pk},
   success:function(data,textStatus){
      $("#logsresult%s").html("")
      $("#logsresult%s").append("选择一个点击下载吧<hr>" + data );
	 
      $("#logsguanbi%s").removeAttr("disabled");
      //  logsguanbi_moban%s();
   }

   });

	
	
};


function logsguanbi_moban%s(){
    //点关闭后，刷新
     $('#logsmyModal%s').on('hide.bs.modal',
    function() {
        window.location.reload();
    })
    
   }




</script>



"""  % (pk,pk,pk,pk,pk,pk,pk,pk,pk,pk)

    return queding_peizhi_moban + queding_peizhi_moban2 +queding_peizhi_moban3 +queding_peizhi_moban4  +queding_peizhi_moban6
