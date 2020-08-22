package org.raygoza.json;

import java.util.Collections;
import java.util.Vector;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class JSONUtils {

	
	
	public static void sortArrayByStringField(JSONArray array,String field) {
		
		JSONArray array2 = new JSONArray();
		array2.addAll(array);
		array.clear();
		
		Vector<String> original_order= new Vector<String>();
		Vector<String> sorted = new Vector<String>();
		
		for(int i=0; i < array2.size(); i++) {
			JSONObject json = array2.getJSONObject(i);
			original_order.add(json.getString(field));
			sorted.add(json.getString(field));
		}
		
		Collections.sort(sorted);
		
		for(int i=0; i< sorted.size();i++) {
			int idx = original_order.indexOf(sorted.elementAt(i));
			array.add(array2.get(idx));
		}
		
		
	}
	
	
}
