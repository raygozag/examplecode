package org.raygoza.kegg;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class PathwaysForOrganismRetriever {

	public static void main(String[] args) throws Exception{
		
		/*URL url = new URL("http://www.kegg.jp/kegg-bin/search_pathway_text?map="+args[0]+"&keyword=&mode=1&viewImage=false&perPage=2000");
		
		
		
		
		
		
		
		
		String xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
		
		
				
		
		  /////////////////
        //Output the XML

        //set up a transformer
        TransformerFactory transfac = TransformerFactory.newInstance();
        Transformer trans = transfac.newTransformer();
        trans.setOutputProperty(OutputKeys.INDENT, "yes");

        //create string from xml tree
        StringWriter sw = new StringWriter();
        StreamResult resultx = new StreamResult(sw);
        DOMSource source = new DOMSource(doc);
        trans.transform(source, resultx);
        String xmlString = sw.toString();

        //print xml
        FileWriter wr = new FileWriter(args[0]+".xml");
        wr.write(xmlString);
        wr.close();
		
		*/
		
		
		
	}
	
}
