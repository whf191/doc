<?php
header("content-type:text/html;charset=gbk");
/*
 * Created on 2018-1-31
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */



?>
	<div class="row">

				<div class="col-md-12">
					<div style="display:block;margin:0 auto;">


	<form class="form-horizontal" role="form" action="/new_cj/admin_login.php" method="post">



	<div class="form-group">
		<label for="firstname" class="col-sm-2 control-label">用户</label>
		<div class="col-sm-10">
			<input type="text"  class="form-control input-lg" id="firstname"  name="username"
				   placeholder="请输入用户名"  style="width:30%;">
		</div>
	</div>
	<div class="form-group">
		<label for="lastname" class="col-sm-2 control-label">密码</label>
		<div class="col-sm-10">
			<input type="password"  class="form-control" id="lastname"  password="password" name="password"
				   placeholder="请输入密码" style="width:30%;"  >
		</div>
	</div>
	<div class="form-group">
		<div class="col-sm-offset-2 col-sm-10">
			<div class="checkbox">
				<label>
					<input type="checkbox"> 请记住我
				</label>
			</div>
		</div>
	</div>
	<div class="form-group">
		<div class="col-sm-offset-2 col-sm-10">
			<button type="submit" class="btn btn-default">登录</button>
		</div>
	</div>
</form>
					</div>

				</div>

				</div>