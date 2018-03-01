package com.weibo.db.tables;

public class ShouYeZhanShi {
		Integer id;
		String name;
		String touxiang;
		String backgroudimage;
		String desc;
	
		public ShouYeZhanShi(Integer id,String name,String desc,String touxiang,String backgroudimage ) {
			// TODO Auto-generated constructor stub
		this.id = id;
		this.name = name;
		this.desc = desc;
		this.touxiang = touxiang;
		this.backgroudimage = backgroudimage;
		}
		public Integer getId() {
			return id;
		}
	public String getName() {
		return name;
	}
	
	public String getDesc() {
		return desc;
	}
	
	public String getTouxiang() {
		return touxiang;
	}
	public String getBackgroudimage() {
		return backgroudimage;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
