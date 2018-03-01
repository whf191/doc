package com.weibo.db.mybatis.impl;

import java.io.InputStream;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class MyBatisPid {

	SqlSession session1;
	
	public MyBatisPid() {
		// TODO Auto-generated constructor stub
		System.out.println(System.getProperty("user.dir"));
		String resource = "com/weibo/db/mybatis/xmlmapping/conf.xml";
		
		InputStream is = MyBatisPid.class.getClassLoader().getResourceAsStream(resource);
		
		SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(is);
		
		SqlSession session = sessionFactory.openSession();
		this.session1 = session;
		

		
	}
	
	public SqlSession getSession1() {
		return session1;
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
