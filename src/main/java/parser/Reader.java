package parser;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class Reader {

    Reader(String fileName){
        Path path = Paths.get(fileName);

        try {
            BufferedReader reader = Files.newBufferedReader(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
