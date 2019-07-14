package parser;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class collectData {


    public static ArrayList<String> getData(String searchID, String searchDateOpen, String SearchDateClose) {

        ArrayList<String> returnList = new ArrayList<String>();

        try {
            Scanner scan = new Scanner(new File("src/main/resources/data/produktionsdata.csv"));
            while(scan.hasNextLine()) {

                String[] ID = scan.nextLine().split(";");

                if (ID[0].equals(searchID) && ID[2].equals(searchDateOpen)) {
                    for (int i = 10; i < 57; i = i+2) {
                        returnList.add(ID[i]);
                        System.out.println(ID[i]);
                    }
                }



            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return returnList;
    }

}


