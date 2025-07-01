class Solution {
    public int missingNumber(int[] nums) {
        int length = nums.length;
        int expectedSum = (int)(length*(length+1))/2;
        int actualSum = 0;
        for(int i=0;i<length;i++){
            actualSum+=nums[i];
        }
        return expectedSum-actualSum;
    }
}
