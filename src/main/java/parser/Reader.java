package parser;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class Reader {

    private BufferedReader reader;

    Reader(String fileName){

        Path path = Paths.get(fileName);

        try {
            reader = Files.newBufferedReader(path);
            System.out.println("info från bufferedReader: " + reader.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
