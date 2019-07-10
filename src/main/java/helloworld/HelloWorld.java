package helloworld;

import java.io.File;
import java.util.Scanner;

public class HelloWorld {

    /**
     *
     * main.java
     *
     * @author Filip Alberius <filip@alberius.se>, Samuel Alberius <samuel@alberius.se>
     *
     */

    private static String fileName;

    public static void main(String[] args) {

        fileName ="\\Users\\Samuel Alberius\\Desktop";
        File file = new File(fileName);

        try {
            Scanner fileReader = new Scanner(file);
            String line = fileReader.nextLine();
            String[] parts = line.split(";");
            String ID = parts[0];
            System.out.println(ID);

        } catch (Exception e) {
            System.out.println(e.toString());
        }


    }
}
