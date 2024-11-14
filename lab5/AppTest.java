import org.junit.Assert;
import org.junit.Test;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class AppTest {

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

    @Test
    public void testProblem1() {
        problem1 app = new problem1();

        try (BufferedReader reader = new BufferedReader(new FileReader("./testProblem1.txt"))) {
            String line = reader.readLine();
            String[] tokens = line.split(":");
            int number = parseIntFromString(tokens[0]);

            int expectedNumber = parseIntFromString(tokens[1]);

            int Answer = app.fibonacci(number);

            reader.close();
            Assert.assertEquals(expectedNumber, Answer);

        } catch (IOException e) {
            e.printStackTrace();
            Assert.fail("Error");
        }
    }

    @Test
    public void testknap() {
        knapsack app = new knapsack();

        try (BufferedReader reader = new BufferedReader(new FileReader("./testknap.txt"))) {
            String line = reader.readLine();
            String[] tokens = line.split(":");
            int[] weights = parseArrayFromString(tokens[0]);
            int[] values = parseArrayFromString(tokens[1]);
            int capacity = parseIntFromString(tokens[2]);
            int expectedAnswer = parseIntFromString(tokens[3]);
            System.out.println(expectedAnswer);
            int Answer = app.knapsacksol(weights, values, capacity);
            reader.close();
            Assert.assertEquals(expectedAnswer, Answer);

        } catch (IOException e) {
            e.printStackTrace();
            Assert.fail("Error");
        }
    }
}
