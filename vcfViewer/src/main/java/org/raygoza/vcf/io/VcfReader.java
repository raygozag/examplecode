package org.raygoza.vcf.io;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import org.apache.commons.io.IOUtils;
import org.raygoza.vcf.model.VcfEntry;
import org.raygoza.vcf.model.VcfModel;

public class VcfReader {

	
	
	public VcfReader() {
		
	}
	
	public VcfModel readModel(String filename) throws FileNotFoundException,IOException {
		
		BufferedReader rd = new BufferedReader(new FileReader(filename));
		VcfModel model = new VcfModel();
		model.setModel_name(filename);
		
		String line="";
		String chrom ="";
		while(true) {
			line = rd.readLine();
			if(line==null) break;
			
			if(line.startsWith("#")) continue;
			System.out.println(line);
			
			String[] values = line.split("\t");
			
			if(chrom!=values[0]) chrom=values[0];
			
			VcfEntry entry = new VcfEntry();
			
			entry.setStart(Long.parseLong(values[1]));
			entry.setRef(values[3].trim());
			entry.setAlt(values[4].trim());
			if(!values[5].trim().equals(".")){
				//entry.setQuality(Double.parseDouble(values[5].trim()));
			}else {
				entry.setQuality(0.0);
			}
			Properties props = new Properties();
			props.load(IOUtils.toInputStream(values[7].replace(";", "\n")));
			entry.setInfo(props);
			model.addEntry(chrom, entry);
		}
				
		return model;
	}
	
	
}
