package org.raygoza.bx.go.api;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.Vector;





import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class GoDatabase {

	private Connection conn;
	private Statement st;
	
	public GoDatabase(String host,int port, String uname, String pwd,String db) throws Exception{
		try {
			conn = DriverManager.getConnection("jdbc:mysql://"+host+":"+port+"/"+db, uname, pwd);
			
			st = conn.createStatement();
			
		}catch(Exception ex) {
			throw ex;
		}
	}
	
	
	
	public JSONObject getOrganismInfo(long ncbi_taxa_id) throws Exception{
		
		
		
		ResultSet rs = st.executeQuery("select * from species where ncbi_taxa_id="+ncbi_taxa_id);
		
		JSONObject org = new JSONObject();
		
		ResultSetMetaData rsm = rs.getMetaData();
		Vector<String> cols =  new Vector<String>();
		
		for(int i=1; i<= rsm.getColumnCount(); i++ ) {
			cols.add(rsm.getColumnLabel(i));
		}
		rs.next();
		for(String field:cols) {
			org.put(field, rs.getString(field));
		}
		
		return org;
		
		
		
	}
	
	public JSONArray getProductsForOrganism(long orgid) throws Exception{
		JSONArray array = new JSONArray();
		
		ResultSet rs = st.executeQuery("select * from gene_product where species_id="+orgid);
		
		ResultSetMetaData rsm = rs.getMetaData();
		Vector<String> cols =  new Vector<String>();
		
		for(int i=1; i<= rsm.getColumnCount(); i++ ) {
			cols.add(rsm.getColumnLabel(i));
		}
		
		while(rs.next()) {
			
			JSONObject product = new JSONObject();
			
			for(String field:cols) {
				product.put(field, rs.getString(field));
			}
			
			array.add(product);
			
			
		}
		
		return array;
		
	}
	
	public JSONArray getGoTermForProduct(long id) throws Exception{
		JSONArray array = new JSONArray();

		ResultSet rs = st.executeQuery("select acc from term where id in (select term_id from association where gene_product_id="+id+")");
		
		while(rs.next()) {
			array.add(rs.getString(1));
		}
		
		return array;
	}
	
	
	public boolean isConnected() throws Exception{
		return !conn.isClosed();
	}
	
}
