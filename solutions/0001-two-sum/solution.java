class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ans[]=new int[2];
        int n=nums.length,flag=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    ans[0]=i;
                    ans[1]=j;
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            {
                break;
            }
        }
        return ans;
    }
}
