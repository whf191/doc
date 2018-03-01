package com.weibo.log;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;



public class Test {


	
	
	
	
	public static void main(String[] args) {


	PropertyConfigurator.configure("log4j.properties");
	Logger	Log = Logger.getLogger(Test.class);
	Log.info("feiji2222222............");
		
		//System.out.println(System.getProperty("user.dir"));
		
	}

}
