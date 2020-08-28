/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author AKS
 */

import org.json.JSONObject;
import org.json.XML;
import java.io.*;


public class XML_to_Json {
    static String line="",str="";
    public static void main(String[] args) throws IOException {
        String link = "customer.xml";
        BufferedReader br = new BufferedReader(new FileReader(link));
        while ((line = br.readLine()) != null) 
        {   
            str+=line;  
        }
        JSONObject jsondata = XML.toJSONObject(str);
        //System.out.println(jsondata);
        try (FileWriter file = new FileWriter("Output.json")) {
			file.write(jsondata.toString());
			System.out.println("Successfully Copied JSON Object to File...");
			//System.out.println("\nJSON Object: " + jsondata);
		}

    }
    
}
