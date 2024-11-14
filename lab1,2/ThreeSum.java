import java.io.*;
import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // массивыг эрэмбэлэх
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1; // The left pointer
            int right = nums.length - 1; // The right pointer
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for the left pointer
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    // Skip duplicates for the right pointer
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Move both pointers
                    left++;
                    right--;
                } else if (sum < 0) {
                    // If sum is less than zero, move the left pointer to increase the sum
                    left++;
                } else {
                    // If sum is greater than zero, move the right pointer to decrease the sum
                    right--;
                }
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        // Input and output file paths
        String inputFilePath = "input2.txt";
        String outputFilePath = "output2.txt";

        List<Integer> numsList = new ArrayList<>();
        
        // Reading input from file
        try (Scanner scanner = new Scanner(new File(inputFilePath))) {
            while (scanner.hasNextInt()) {
                numsList.add(scanner.nextInt());
            }
        } catch (FileNotFoundException e) {
            System.out.println("Input file not found: " + inputFilePath);
            return;
        }

        // Convert List<Integer> to int[]
        int[] nums = numsList.stream().mapToInt(i -> i).toArray();

        // Create a ThreeSum object and find the triplets
        ThreeSum solution = new ThreeSum();
        List<List<Integer>> result = solution.threeSum(nums);

        // Writing result to output file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath))) {
            for (List<Integer> triplet : result) {
                writer.write(triplet.toString());
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error writing to output file: " + outputFilePath);
        }
    }
}
