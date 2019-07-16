package parser;

import java.io.File;

public class Main {

    public static void main(String[] args) {

       CSVreader reader = new CSVreader("734012530000000438", "201703130000", "201703130000");
       Double[] values = reader.getData();

       for (int i = 0; i<values.length; i++) {
           System.out.println("timme " + i + ": " + values[i]);
       }
    }
}
