package com.weibo.db.shouyezhanshi;

import java.io.File;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.xml.ws.Dispatch;

import org.apache.ibatis.session.SqlSession;

import com.weibo.db.mybatis.impl.MyBatisId;
import com.weibo.db.mysql.MysqlDemo;
import com.weibo.db.tables.ContentMyBatis;
import com.weibo.db.tables.GuanzhuFenshi;
import com.weibo.db.tables.GuanzhuFenshiMyBatis;
import com.weibo.log.LogMain;

/**
 * Servlet implementation class ShouYeZhanShi
 */
@WebServlet("/syzs")
public class ShouYeZhanShi extends HttpServlet {
	private static final long serialVersionUID = 1L;

       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ShouYeZhanShi() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub

		ServletContext  sc  = 	this.getServletContext();
        String log4j_file = sc.getRealPath("/") + "\\WEB-INF\\classes" + "\\log4j.properties";
  
		LogMain logMain = new LogMain(log4j_file);
//		logMain.info("加载配置文件");
	
		
		
		
		MyBatisId myBatisId = new MyBatisId();
		
		SqlSession sqlSession = myBatisId.getSession1();
		
		String statement = "com.weibo.db.mybatis.xmlmapping.getGuanzhuFenshiMyBatis";
		GuanzhuFenshiMyBatis guanzhuFenshi = sqlSession.selectOne(statement);
		
		String statement2 = "com.weibo.db.mybatis.xmlmapping.getContentMyBatis";
		
		List<ContentMyBatis> contentMyBatis =   sqlSession.selectList(statement2);
		
	
		
		request.setAttribute("contentMyBatis", contentMyBatis);
		request.setAttribute("guanzhufenshi", guanzhuFenshi);
		
		
		
		

		System.out.println(guanzhuFenshi);
		
		
		ArrayList shouyezhanshi = new ArrayList();
				
		MysqlDemo mysqlDemo = new MysqlDemo();
//		MysqlDemo mysqlDemo2 = new MysqlDemo();
		
		ResultSet rSet =   mysqlDemo.select("SELECT user.id ,user.name,weibo.`desc`,`user`.touxiang,shouyezhanshi.`background-iamge` backgroundiamge"
				+ " from user JOIN weibo ON user.id= weibo.id JOIN shouyezhanshi ON shouyezhanshi.id = user.id");
		
		
//		ResultSet guanzhu_fenshi = mysqlDemo2.select("SELECT guanzhu.count guanzhu,fenshi.count fenshi from fenshi ,guanzhu");
//		
//		try {
//			while (guanzhu_fenshi.next()) {
//				Integer guanzhu = guanzhu_fenshi.getInt("guanzhu");
//				Integer fenshi = guanzhu_fenshi.getInt("fenshi");
//				
//				GuanzhuFenshi guanzhuFenshi = new GuanzhuFenshi(guanzhu, fenshi);	
//				request.setAttribute("guanzhufenshi", guanzhuFenshi);
//				
//			}
//			
//		} catch (SQLException e1) {
//			// TODO Auto-generated catch block
//			e1.printStackTrace();
//		}
//		finally {
//			
//				mysqlDemo2.colse();
//	
//		}
			
		try {
			while (rSet.next()) {
				Integer id = rSet.getInt("id");
				String name = rSet.getString("name");
				String desc = rSet.getString("desc");
				String touxiang = rSet.getString("touxiang");
				String backgroudimage =  rSet.getString("backgroundiamge");
				com.weibo.db.tables.ShouYeZhanShi shouYeZhanShi2 =  new com.weibo.db.tables.ShouYeZhanShi(id, name, desc, touxiang, backgroudimage);
				shouyezhanshi.add(shouYeZhanShi2);
				
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		finally {
			mysqlDemo.colse();
		}
		request.setAttribute("shouyezhanshi", shouyezhanshi.get(0));
		System.out.println(shouyezhanshi.get(0));
		
		RequestDispatcher dispatcher = request.getRequestDispatcher("/jsp/index.jsp");
		dispatcher.forward(request, response);
		
		
		//	response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
