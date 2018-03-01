package com.weibo.log;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;

public class LogMain {
	private   Logger log;
	
	public LogMain() {
		// TODO Auto-generated constructor stub
		//��ȡ��ǰ·��
		//System.out.println(System.getProperty("user.dir"));
		PropertyConfigurator.configure("log4j.properties");
		this.log = Logger.getLogger(LogMain.class);
	
	}
	
	
	public LogMain(String log4j) {
		
		PropertyConfigurator.configure(log4j);
		this.log = Logger.getLogger(LogMain.class);
	}
	
	
	
	public void info(String message){
		log.info(message);
	}
	
	public void error(String message){
		log.error(message);
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LogMain logger = new LogMain();
		logger.info("ff");
		
		

	}

}
