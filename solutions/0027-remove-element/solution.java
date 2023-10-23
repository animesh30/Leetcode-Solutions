class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length==0){
            return 0;
        }
        int j=nums.length-1;
        while(j>0&&nums[j]==val){
            j--;
        }
        // System.out.println(nums.length+" "+j);
        int i=0;
        while(i<j){
            if(nums[i]==val){
                int temp = nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                j--;
                if(nums[j]==val){
                    while(j>0&&nums[j]==val){
                        j--;
                    }
                }
            }
            i++;
        }
        i=0;
        while(i<nums.length&&nums[i]!=val){
            i++;
        }
        return i;
    }
}
