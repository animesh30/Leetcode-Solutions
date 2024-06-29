class Solution {
    public int majorityElement(int[] nums) {
        int majEle=nums[0],majEleOcc=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]==majEle){
                majEleOcc++;
            }
            else{
                majEleOcc--;
                if(majEleOcc==0){
                    majEleOcc=1;
                    majEle=nums[i];
                }
            }
        }
        return majEle;
    }
}
