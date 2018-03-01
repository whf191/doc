package liziqi;

import java.io.InputStream;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.weibo.db.tables.GuanzhuFenshiMyBatis;
public class TestMybatis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		String resource = "com/weibo/db/mybatis/xmlmapping/conf.xml";
		
		InputStream is = TestMybatis.class.getClassLoader().getResourceAsStream(resource);
		
		SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(is);
		
		SqlSession session = sessionFactory.openSession();
		
		String statement = "com.weibo.db.mybatis.xmlmapping.getGuanzhuFenshiMyBatis";
		GuanzhuFenshiMyBatis user = session.selectOne(statement);
		System.out.println(user+ "");
		
	}

}
