package org.raygoza.vcf.model;

import java.io.StringReader;
import java.util.Properties;

public class Feature {

	String name;
	String strand;
	int start;
	int end;
	
	public Feature(String entry) {
		try {
		String[] values = entry.split("\t");
		Properties props = new Properties();
		props.load(new StringReader(values[8].replace(";", "\n")));
		name= props.getProperty("locus_tag");
		start = Integer.parseInt(values[3]);
		end= Integer.parseInt(values[4]);
		strand = values[6];
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getStrand() {
		return strand;
	}
	public void setStrand(String strand) {
		this.strand = strand;
	}
	public int getStart() {
		return start;
	}
	public void setStart(int start) {
		this.start = start;
	}
	public int getEnd() {
		return end;
	}
	public void setEnd(int end) {
		this.end = end;
	}
	
	
	
	
}
