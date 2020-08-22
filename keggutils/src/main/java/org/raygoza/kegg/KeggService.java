package org.raygoza.kegg;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.HashMap;
import java.util.Vector;

import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.tuple.ImmutablePair;
import org.apache.commons.lang3.tuple.MutablePair;
import org.apache.commons.lang3.tuple.Pair;

public class KeggService {

	private String base_url="";
	private HttpClient client;
	
	
	public KeggService(String base) {
		base_url=base;
		
		client = new HttpClient();
	}
	
	
	
	public String getOrganismName(String orgcode)  throws Exception{
		
		GetMethod get = new GetMethod(base_url+"info/"+orgcode);
		client.executeMethod(get);
		
		String[] values = IOUtils.toString(get.getResponseBodyAsStream()).split("           ");
		
		
		return values[1].substring(0,values[1].indexOf("KEGG"));
	}
	
	
	public Vector<Pair<String, String>> getPathwaysForOrganism(String org) throws Exception{
		
		Vector<Pair<String, String>> paths = new Vector<Pair<String,String>>();
		
		GetMethod get = new GetMethod(base_url+"/list/pathway/"+org);
		
		client.executeMethod(get);
		
		StringReader str = new StringReader(IOUtils.toString(get.getResponseBodyAsStream()));
		BufferedReader rd = new BufferedReader(str);
		String line="";
		
		while(true) {
			line=rd.readLine();
			if(line==null) break;
			String[] values = line.split("	"); 
			Pair<String, String> path = new ImmutablePair<String, String>(values[0].replace("path:", ""), values[1]);
			paths.add(path);
			
		}
		
		
		return paths;
	}
	
	
	
	public Vector<Pair<String,String>> getGeneListForPathway(String path_id) throws Exception{ 
		
		Vector<Pair<String,String>> genes = new Vector<Pair<String,String>>(); 
	
		GetMethod get = new GetMethod(base_url+"link/genes/path:"+path_id);
		client.executeMethod(get);
		
		StringReader strd = new StringReader(IOUtils.toString(get.getResponseBodyAsStream()));
		
		BufferedReader rd = new BufferedReader(strd);
		
		String line = "";
		
		while(true) {
			line= rd.readLine();
			if(line==null) break;
			
			String[] values = line.split("	");
			genes.add(getGeneInfo(values[1].trim()));
			
		}
		
		
		return genes;
	}
	
	/**
	 * Must include orgid:
	 * 
	 * orgid:geneid
	 * 
	 * @param geneId
	 * @return
	 * @throws Exception
	 */
	
	
	public Pair<String,String> getGeneInfo(String geneId) throws Exception{
		
		
		GetMethod get = new GetMethod(base_url+"list/"+geneId);
		
		client.executeMethod(get);
		
		String res = IOUtils.toString(get.getResponseBodyAsStream());
		
		String[] values = res.replace("	", ";").trim().split(";");
		
		Pair<String ,String> gene =new MutablePair<String, String>(" \t ", "");
		if(values.length>3) {
			gene = new MutablePair<String, String>(values[0].trim()+"\t"+values[1].trim(),values[2].trim());
		}else {
			gene = new MutablePair<String, String>(values[0].trim()+"\t ",values[1].trim());
		}
		
		return gene;
	}
	
	
	
	public HashMap<String, String> getGeneDetails(String geneId) throws Exception{
		
		HashMap<String, String> feats = new HashMap<String, String>();
		
		GetMethod get = new GetMethod(base_url+"get/"+geneId);
		
		client.executeMethod(get);
		
		String line="";
		
		BufferedReader rd = new BufferedReader(new InputStreamReader(get.getResponseBodyAsStream()));
		int k=0;
		while(true) {
			line = rd.readLine();
			if(line==null) break;
			
			if(line.trim().startsWith("AASEQ")) break;
			
			if(k==1) {
				line = line.trim().toLowerCase();
				String[] vals=line.split(":");
				if(vals.length>1) {
					feats.put(vals[0].trim(), vals[1].trim());
				}
			}
			
			if(line.startsWith("DBLINKS")) {
				line = line.replace("DBLINKS","").trim().toLowerCase();
				String[] vals=line.split(":");
				feats.put(vals[0].trim(), vals[1].trim());
				
				k=1;
			}
			
		}
		
		
		return feats;
	}
	
	
}
