class Solution {
    public int removeDuplicates(int[] nums) {
        int prevEle=nums[0],i=1;
        for(int j=1;j<nums.length;j++){
            if(nums[j]!=prevEle){
                nums[i]=nums[j];
                prevEle=nums[j];
                i++;
            }
        }
        i=0;
        while(i<nums.length-1&&nums[i]<nums[i+1]){
            i++;
        }
        return i+1;
    }
}
