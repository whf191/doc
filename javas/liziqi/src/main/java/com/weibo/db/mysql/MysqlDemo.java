package com.weibo.db.mysql;

import java.security.Identity;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;


import com.weibo.log.LogMain;

public class MysqlDemo {
	private static LogMain log_main = new LogMain();
	private static  String JDBC_DRIVE="com.mysql.jdbc.Driver";
	private static  String  DB_URL = "jdbc:mysql://192.168.0.17:3306/weibo?characterEncoding=utf8&useSSL=false";
	
	private static  String user = "admin";
	private static  String pass = "wanwan";
	
	Connection conn =null;
	
	java.sql.Statement  statement= null;
	
	//默认构造器
	public MysqlDemo() {
		// TODO Auto-generated constructor stub
		this.conn = openconn();
		try {
			statement = conn.createStatement();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	//参数化构造器
	public MysqlDemo( String JDBC_DRIVE, String DB_URL,String user ,String  pass) {
		  this.JDBC_DRIVE = JDBC_DRIVE;
		  this.DB_URL = DB_URL;
		  this.user = user;
		  this.pass = pass;
		  this.conn = openconn();
		  
			try {
				statement = conn.createStatement();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
	}
	
	//打开返回连接对象
	 public  Connection  openconn() {
		 
		 try {
			Class.forName(JDBC_DRIVE);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			conn = DriverManager.getConnection(DB_URL, user,pass);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		 
		return conn;
	
	 }
	
	public ResultSet select(String sql) {
		ResultSet rSet = null;
		try {
			rSet = statement.executeQuery(sql);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return rSet;
		
	}
	
	public Boolean   Insert(String sql) {
		Boolean boolean1 = true;
		
		try {
			statement.executeQuery(sql);
			conn.commit();
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			boolean1 = false;
			try {
				conn.rollback();
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
		
		return boolean1;
	}
	
	
	
   public  void colse() {
	   log_main.info("连接开始关闭.....hashCode->" + this.hashCode());
	   
	   try {
		statement.close();
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		System.out.println("11111111111");
		e.printStackTrace();
	}
	   try {
		conn.close();
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		System.out.println("2");
		e.printStackTrace();
	}
	   log_main.info("连接结束关闭.....hashCode->" + this.hashCode());
	   
   }
	
	
	
	public static void main(String[] args) throws SQLException, CloneNotSupportedException {
		// TODO Auto-generated method stub

		MysqlDemo mysqlDemo = new MysqlDemo();
		ResultSet rSet =  mysqlDemo.select("select * from idc_hosts limit 10,9");
		
		
		while (rSet.next()) {
			System.out.println(rSet.getInt("id"));
			
		}
		mysqlDemo.colse();

	}

}
