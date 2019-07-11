package parser;

import java.io.File;
import java.util.Scanner;

public class Reader2 {

    private Scanner scan;

   Reader2(String fileName){

        File file = new File(fileName);

        try {
            scan = new Scanner(file);
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("info från scanner: " + scan.nextLine());

    }
}
