package org.raygoza.bx.rPrimer;

import java.awt.BorderLayout;
import java.io.BufferedReader;
import java.io.StringReader;

import javax.swing.JEditorPane;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import org.apache.commons.lang.StringUtils;

public class ResultPanel extends JPanel {

	
	JEditorPane area = new JEditorPane();
	String html ="";
	
	public ResultPanel(String text) {
		
		setLayout(new BorderLayout());
		
		JScrollPane jsp = new JScrollPane();
		text = text.replace("</html>", "").replace("</body>", "");
		
		area = new JEditorPane();
		area.setEditable(false);
		area.setContentType("text/html");
		String[] k = text.split("\n");
		try {
			area.setText(processString(text));
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		html = text;
		jsp.setViewportView(area);
		
		add(jsp,BorderLayout.CENTER);
		
		
		
	}
	
	public String getText() {
		return area.getText();
	}
	
	public String processString(String text) throws Exception{
		String res = "";
		
		BufferedReader rd = new BufferedReader(new StringReader(text));
		int state=0;
		int state2=0;
		String line ="";
		
		while(true) {
			line = rd.readLine();
			if(line==null) break;
			if(line.contains("<body")) {
				state=1;
				continue;
			}
			if(line.contains("</body")) {
				state=0;
				continue;
			}
			
			if(state==1) {
				if(line.trim().matches("^[<]+$")) {
					String txt = line.trim();
					String rep = StringUtils.repeat("&lt;", txt.length());
					line = line.replace(txt, rep);
				}
					res+=line+"\n";
				
				
				
				
			}
			
		}
		
		
		return res;
		
		
	}
	
	
	
	
}
