<?php
header("Content-Type:text/html;charset=gbk");
/*
 * Created on 2018-1-30
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */
?>
<?php

class M_mysql{


 	var $mysqlhost="sql102.byethost18.com";
	var $mysqldb="b18_21500339_www";
	var $username="b18_21500339";
	var $password="wan5845201314";


 	var $conn;
	function __construct ($bianma="gbk") {

		     if (php_uname('s') == "Windows NT" or true) {
				//默认windows平台,作为开发环境,线上环境走linux
				$this->mysqlhost="119.23.69.52";
			 	$this->username = "admin";
			 	$this->password = "wanwan";
			 	$this->mysqldb = "cmdb";

			}


			$conn= new mysqli($this->mysqlhost,$this->username,$this->password,$this->mysqldb);
			if ($conn->connect_error){
				die("error...:" . $conn->connect_error);

			}
			else{
				if ($bianma) {
				mysqli_set_charset($conn,$bianma);
				}
				else {
					mysqli_set_charset($conn,"gbk");
				}

              $this->conn = $conn;


			}
	}

  	function select ($sql) {

      $result = $this->conn->query($sql);
      return $result;


	}

	function update($sql){

		//$sql =  addslashes($sql);
		mysqli_query($this->conn,"set names 'utf8';");
		$r1 = mysqli_query($this->conn,$sql);
		echo mysqli_error($this->conn);
		return $r1;

	}

	function into($sql){
		//php中文插入还必须得utf8...
		mysqli_query($this->conn,"set names 'utf8';");
		if (mysqli_query($this->conn,$sql) == TRUE ) {
			return TRUE;

		}
		else {
			echo mysqli_error($this->conn);
			return FALSE;
		}

	}


	function colse () {

		mysqli_close($this->conn);

	}





}




?>