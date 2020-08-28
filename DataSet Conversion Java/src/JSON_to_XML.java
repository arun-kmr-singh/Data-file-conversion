


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author AKS
 */

//import static XML_to_Json.str;
import java.io.*;
import org.json.JSONObject;
import org.json.XML;


public class JSON_to_XML {
    static String line="",str="";
    public static void main(String[] args) throws IOException {
        
            String link = "demo.json";
            BufferedReader br = new BufferedReader(new FileReader(link));
        while ((line = br.readLine()) != null) 
        {   
            str+=line;  
        }
        JSONObject jsondata = new JSONObject(str);
        //System.out.println(jsondata);
        try (FileWriter file = new FileWriter("Out.xml")) {
			file.write(XML.toString(jsondata));
			System.out.println("Successfully Copied XML to File...");
			//System.out.println("\nJSON Object: " + jsondata);
		}
            
    }
    
}
