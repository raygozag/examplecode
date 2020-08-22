package org.raygoza.kegg;

import java.io.FileWriter;
import java.io.StringWriter;
import java.net.URL;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Vector;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.tuple.Pair;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class GenePathwaysRetriever {

	
	public static void main(String[] args)  throws Exception{
		
		String org=args[0];
		
		KeggService service = new KeggService("http://rest.kegg.jp/");
		
		
		DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
        Document doc = docBuilder.newDocument();
		
		
        Element root = doc.createElement("organism");
        
        String name = service.getOrganismName(org).trim();
        
        root.setAttribute("id", org);
        root.setAttribute("name", name);
        
        doc.appendChild(root);
        
        
        Vector<Pair<String, String>> pathways = service.getPathwaysForOrganism(org);
        
        for(int i=0; i < pathways.size(); i++) {
        	Element pathway = doc.createElement("pathway");
        	pathway.setAttribute("id", pathways.elementAt(i).getLeft().trim());
        	pathway.setAttribute("name", pathways.get(i).getRight().replace(" - "+name, "").trim());
        	root.appendChild(pathway);
        	System.out.println( pathways.get(i).getRight().replace(" - "+name, "").trim() +"---"+ i +" ---"+pathways.size());
        	Vector<Pair<String, String>> genes = service.getGeneListForPathway( pathways.elementAt(i).getLeft().trim());
        	
        	for(int k=0;k< genes.size(); k++) {
        		
        		Element gene = doc.createElement("gene");
        		String[] vals = genes.get(k).getLeft().split("\t");
        		gene.setAttribute("symbol", vals[1]);
        		gene.setAttribute("id", vals[0]);
        		gene.setAttribute("name", genes.get(k).getRight());
        		
        		HashMap<String, String> ft = service.getGeneDetails(vals[0]);
        		
        		Iterator<String> it = ft.keySet().iterator();
        		
        		while(it.hasNext()) {
        			String key = it.next();
        		
        			gene.setAttribute(key.replace(" ", ""), ft.get(key));
        		}
        		
        		pathway.appendChild(gene);
        	}
        	
        	//if(i==0) {
        		//break;
        	//}
        	
        }
        
        
        
		
		
        /////////////////
        //Output the XML

        //set up a transformer
        TransformerFactory transfac = TransformerFactory.newInstance();
        Transformer trans = transfac.newTransformer();
        trans.setOutputProperty(OutputKeys.INDENT, "yes");

        //create string from xml tree
        StringWriter sw = new StringWriter();
        StreamResult result = new StreamResult(sw);
        DOMSource source = new DOMSource(doc);
        trans.transform(source, result);
        String xmlString = sw.toString();

        
    
        
        //print xml
        FileWriter wr = new FileWriter(args[1]);
        wr.write(xmlString);
        wr.close();
	
		
	}
	
	
	
}
