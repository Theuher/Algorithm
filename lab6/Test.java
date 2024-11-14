import org.junit.Assert;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Test {
    private int[] parseArrayFromString(String line) {
        String[] parts = line.trim().split(",\\s*");
        int[] array = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            array[i] = Integer.parseInt(parts[i]);
        }
        return array;
    }

    private int parseIntFromString(String line) {
        String part = line.trim();
        int number;
        number = Integer.parseInt(part);
        return number;
    }


    @org.junit.Test
    public void testProblem() {
        MinimumSearchCost app = new MinimumSearchCost();

        try (BufferedReader reader = new BufferedReader(new FileReader("./test.txt"))) {
            String line = reader.readLine();
            String[] tokens = line.split(":");
            int[] keys = parseArrayFromString(tokens[0]);
            int[] freq = parseArrayFromString(tokens[1]);
            int len = parseIntFromString(tokens[2]);
            int expectedNumber = parseIntFromString(tokens[3]);
            int Answer = app.optimalBST(keys, freq, len);
            reader.close();
            Assert.assertEquals(expectedNumber, Answer);

        } catch (IOException e) {
            e.printStackTrace();
            Assert.fail("Error");
        }
    }
}
