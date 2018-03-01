#coding=utf-8
from  __future__ import unicode_literals
anniu2="""

                            <!DOCTYPE html><html>
                            <head>
                                <meta charset="UTF-8">

                                <script>
                                // 定义个a1的ajax的函数
                                    function a1%s(){


                                    $.ajax({
                                        url:"/qianduan_qi/",
                                        type:"GET",
                                        data:{'ip':"%s"},
                                        success:function(req){
                                             $.messager.progress("close");
                                            alert(req);
                                            window.location.reload();
                                        },

                                        error:function(){


                                            $.messager.progress("close");
                                            alert("不能访问服务器，请联系管理员");
                                        }


                                    });


                                };

                                    $(document).ready(function(){
                                          $("#bb%s").click(function(){

                                            $.messager.progress({text:"正在执行..."});
                                            a1%s();



                                          });
                                        });

                                </script>


                            </head>
                            <button id="bb%s" type="button"  class="btn btn-warning">执行</button>
                            <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/metro/easyui.css">
    <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/mobile.css">
	<link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/icon.css">
	<script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.mobile.js"></script>
                            </html>  """


