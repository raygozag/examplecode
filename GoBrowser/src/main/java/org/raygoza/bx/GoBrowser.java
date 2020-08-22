package org.raygoza.bx;

import java.awt.BorderLayout;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.TreeSet;
import java.util.Vector;

import javax.swing.BoxLayout;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JToolBar;
import javax.swing.ListModel;
import javax.swing.SpringLayout;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import org.apache.commons.lang.StringUtils;
import org.raygoza.bx.go.api.GoDatabase;
import org.raygoza.json.JSONUtils;

import sun.awt.HorizBagLayout;


public class GoBrowser extends JFrame{

	private Connection conn;
	private Statement st;
	private JComboBox taxa_id;
	private GoDatabase db;
	private JList productList;
	private JTextArea infoarea;
	private JFrame me=this;
	private JSONArray products;
	private JTextField searchText;
	private int currfind=0;
	private Vector<Long> ncbi_taxa_ids;
	public GoBrowser() throws Exception{
		
		try {
		 db = new GoDatabase("mysql.ebi.ac.uk", 4085, "go_select", "amigo","go_latest");
		
			
		}catch(Exception ex) {
			JOptionPane.showMessageDialog(this, ex.getMessage());
			System.exit(1);
		}
		compose();
		setSize(500,500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		
	}
	
	
	public void compose()  throws Exception{
		setLayout(new BorderLayout());
		
		JPanel queryPanel = new JPanel();
		JToolBar tools = new JToolBar();
		JButton button = new JButton("copy");
		button.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				 StringSelection selection = new StringSelection(infoarea.getText());
				    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
				    clipboard.setContents(selection, selection);
				
			}
		});
		
		tools.add(button);
		add(tools,BorderLayout.PAGE_END);
		
		JLabel taxa = new JLabel("Select Organism:");
		ncbi_taxa_ids = new Vector<Long>();
		 
		 
		 BufferedReader rd = new BufferedReader(new FileReader(".ncbi_taxa"));
		 
		 String line="";
		 
		 while(true) {
			 line = rd.readLine();
			 if(line==null) break;
			 
			 ncbi_taxa_ids.add(Long.parseLong(line.trim()));
			 
		 }
		 
		 Vector<String> names = new Vector<String>();
		 
		 for(int i=0;i < ncbi_taxa_ids.size(); i++) {
			 
			 JSONObject org =db.getOrganismInfo(ncbi_taxa_ids.elementAt(i));
			 names.add(org.getString("genus")+" "+org.getString("species"));
			 
		 }
		 
		 taxa_id = new JComboBox(names.toArray());
		 
		JButton productsbut = new JButton("get products");
		
		productsbut.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				try {
					if(!db.isConnected()) {
						reconnect();
					}
					JSONObject org = db.getOrganismInfo(Long.valueOf(ncbi_taxa_ids.get(taxa_id.getSelectedIndex())));
					
					me.setTitle(org.getString("genus")+"   "+org.getString("species"));
					
					
					products = db.getProductsForOrganism(org.getLong("id"));
					
					DefaultListModel model = new DefaultListModel();
					JSONUtils.sortArrayByStringField(products, "symbol");
					for(int i=0; i < products.size(); i++) {
						JSONObject json = products.getJSONObject(i);
						model.addElement(json.getString("symbol")+"    "+json.getString("full_name"));
					}
					
					productList.setModel(model);
				} catch (Exception e) {
					JOptionPane.showMessageDialog(null, e.getMessage());
				}
				
			}
		});
		productList= new JList();
		productList.addListSelectionListener(new ListSelectionListener() {
			
			@Override
			public void valueChanged(ListSelectionEvent arg0) {
				
				
				try {
					
					if(!db.isConnected()) {
						reconnect();
					}
					int idx =productList.getSelectedIndex();

					JSONObject json = products.getJSONObject(idx);
					//infoarea.setText();
					//JOptionPane.showMessageDialog(null, json.getString("id"));
					//System.out.println(json.getString("id"));
					
					JSONArray goids= db.getGoTermForProduct(json.getLong("id"));
					 String values="";
					 String[] lines=goids.toString().replace("[", "").replace("]", "").split(",");
					 for(String s:lines) {
						 values+= "                     /db_xref="+s.trim()+"\n";
					 }
					//JOptionPane.showMessageDialog(me, goids.toString());
					 
					infoarea.setText(values.substring(0, values.length() - 1));
				} catch (Exception e) {
					JOptionPane.showMessageDialog(null, e.getMessage());
				}
				
				
			}
		});
		queryPanel.add(taxa);
		queryPanel.add(taxa_id);
		queryPanel.add(productsbut);
		
		JPanel leftPane = new JPanel();
		JScrollPane scroll = new JScrollPane(productList);
		leftPane.setLayout(new BoxLayout(leftPane, BoxLayout.PAGE_AXIS));
		searchText = new JTextField();
		JButton search = new JButton("Find Next");
		search.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				for(int i=currfind; i <products.size();i++) {
					if(products.getJSONObject(i).getString("symbol").toLowerCase().contains(searchText.getText().toLowerCase())) {
						productList.setSelectedIndex(i);
						currfind=i+1;
						productList.ensureIndexIsVisible(i);
					}
				}
				currfind=0; 
				for(int i=currfind; i <products.size();i++) {
					if(products.getJSONObject(i).getString("full_name").toLowerCase().contains(searchText.getText().toLowerCase())) {
						productList.setSelectedIndex(i);
						currfind=i+1;
						productList.ensureIndexIsVisible(i);
					}
				}
				currfind=0; 
			}
		});
		JSplitPane scroll2 = new JSplitPane(JSplitPane.VERTICAL_SPLIT);
		
		leftPane.add(searchText);
		leftPane.add(search);
		scroll2.setTopComponent(leftPane);
		scroll2.setBottomComponent(scroll);
		
		
		
		infoarea = new JTextArea();
		
		
		JSplitPane jsplit = new JSplitPane();
		jsplit.setLeftComponent(scroll2);
		jsplit.setRightComponent(infoarea);
		add(queryPanel,BorderLayout.PAGE_START);
		
		add(jsplit,BorderLayout.CENTER);
	}
	
	private void reconnect() throws Exception{
		db = new GoDatabase("mysql.ebi.ac.uk", 4085, "go_select", "amigo","go_latest");
	}
	
	public static void main(String[] args) throws Exception{
		
		GoBrowser gb= new GoBrowser();
		
		gb.setVisible(true);
		
		
	}
	
	
}
