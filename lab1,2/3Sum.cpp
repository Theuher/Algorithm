#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1; 
            int right = nums.size() - 1; 
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return result;
    }
};

int main() {
    std::ifstream inputFile("input2.txt");
    std::ofstream outputFile("output2.txt");
    
    if (!inputFile.is_open() || !outputFile.is_open()) {
        std::cerr << "Оролт эсвэл гаралтын файлыг нээхэд алдаа гарлаа!" << std::endl;
        return 1;
    }

    std::vector<int> nums;
    int number;
    
    while (inputFile >> number) {
        nums.push_back(number);
    }
    
    Solution solution;
    std::vector<std::vector<int>> result = solution.threeSum(nums);
    
    for (const auto& triplet : result) {
        outputFile << "[";
        for (size_t i = 0; i < triplet.size(); ++i) {
            outputFile << triplet[i];
            if (i < triplet.size() - 1) {
                outputFile << ",";
            }
        }
        outputFile << "]\n";
    }
    
    inputFile.close();
    outputFile.close();
    
    return 0;
}
