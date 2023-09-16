class Solution {
    public int majorityElement(int[] nums) {
        int maxEle = nums[0], maxCount = 1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]==maxEle){
                maxCount++;
            }
            else{
                maxCount--;
                if(maxCount==0){
                    maxCount=1;
                    maxEle=nums[i];
                }
            }
        }
        return maxEle;
    }
}
