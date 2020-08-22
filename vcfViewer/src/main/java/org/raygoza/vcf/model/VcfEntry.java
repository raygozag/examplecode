/**
 * 
 */
package org.raygoza.vcf.model;

import java.util.HashMap;
import java.util.Properties;

/**
 * @author Juan Antonio Raygoza Garay
 *
 */
public class VcfEntry {

	private String ref;
	private String alt;
	private long start;
	private double quality;
	private Properties info = new Properties();
	
	
	public VcfEntry() {
		
	}

	public String getRef() {
		return ref;
	}

	public void setRef(String ref) {
		this.ref = ref;
	}

	public String getAlt() {
		return alt;
	}

	public void setAlt(String alt) {
		this.alt = alt;
	}

	public long getStart() {
		return start;
	}

	public void setStart(long start) {
		this.start = start;
	}

	public double getQuality() {
		return Math.pow(10.0,-(quality/10.0));
	}

	public void setQuality(double quality) {
		this.quality = quality;
	}

	public Properties getInfo() {
		return info;
	}

	public void setInfo(Properties info) {
		this.info = info;
	}
	
	
	
	public String getProperty(String prop) {
		if(info.containsKey(prop)) {
			return info.getProperty(prop);
		}
		return "N/A";
	}
	
	public int getPropertyAsInt(String name) {
		if(info.containsKey(name)) {
		return Integer.parseInt(info.getProperty(name).trim());
		}
		return 0;
	}
	
	
	
	
}
