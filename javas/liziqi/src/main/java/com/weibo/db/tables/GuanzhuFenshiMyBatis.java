package com.weibo.db.tables;

public class GuanzhuFenshiMyBatis {
	public Integer guanzhu;
	public Integer fenshi;
	

	
	public void setFenshi(Integer fenshi) {
		this.fenshi = fenshi;
	}
	
	public void setGuanzhu(Integer guanzhu) {
		this.guanzhu = guanzhu;
	}
	

	
	public Integer getFenshi() {
		return fenshi;
	}
	
	public Integer getGuanzhu() {
		return guanzhu;
	}
	
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "fenshi=" + fenshi + "guanzhu=" + guanzhu;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
