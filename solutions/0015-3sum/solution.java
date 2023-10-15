class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Map<List<Integer>,Integer> map=new HashMap<>();
        List<List<Integer>> ans=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            int j=i+1,k=nums.length-1;
            while(j<k){
                if(nums[i]+nums[j]+nums[k]==0){
                    List<Integer> temp=new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(nums[k]);
                    if(map.containsKey(temp)){

                    }
                    else{
                        map.put(temp,1);
                        ans.add(temp);
                    }
                    j++;
                    k--;
                }
                else if(nums[i]+nums[j]+nums[k]<0){
                    j++;
                }
                else{
                    k--;
                }
            }
        }
        return ans;
    }
}
