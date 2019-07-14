package parser;

import java.io.File;
import java.util.Scanner;

public class CSVreader {

    private final String FILENAME  = "src/main/resources/data/produktionsdata.csv";
    private String date;
    private String endDate;
    private String ID;

    public CSVreader(String ID, String date, String endDate) {

        this.ID = ID;
        this.date = date;
        this.endDate = endDate;

    }

    public Double[] getData() {

        Double[] values = new Double[24];

        try {
            Scanner reader = new Scanner(new File(FILENAME));
            while(reader.hasNextLine()) {
                String[] parts = reader.nextLine().split(";");
                if (parts[0].equals(ID) && parts[2].equals(date)) {
                    int index = 0;
                    for (int i = 10; i < 57; i = i + 2) {
                        values[index] = Double.parseDouble(parts[i].replace(",", "."));
                        index++;
                    }
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return values;
    }
}
