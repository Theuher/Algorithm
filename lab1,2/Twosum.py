class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
        return []
    






















    
def main():
    try:
        with open("input1.txt", "r") as file:
            nums = list(map(int, file.readline().split()))
            target = int(file.readline())
        solution = Solution()
        result = solution.twoSum(nums, target)
        with open("output1.txt", "w") as file:
            if result:
                file.write("{} {}".format(result[0], result[1]))
            else:
                file.write("Hariult baihgui baina")
    
    except IOError as e:
        print("File-iig unshih esvel bichihed aldaa garlaa {}".format(e))

if __name__ == "__main__":
    main()
