package parser;

import java.io.File;

public class Main {

    public static void main(String[] args) {

        Reader reader = new Reader("src/main/resources/data/produktionsdata.csv");

        Reader2 reader2 = new Reader2("src/main/resources/data/produktionsdata.csv");

        collectData.getData("734012530000000438", "201701010000", "201701010000" );

    }
}
