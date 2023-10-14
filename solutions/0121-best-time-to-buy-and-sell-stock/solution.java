class Solution {
    public int maxProfit(int[] prices) {
        int maxPro = 0,len=prices.length;
        int rightMax[]=new int[len];
        for(int i=len-2;i>=0;i--){
            rightMax[i]=Math.max(rightMax[i+1],prices[i+1]);
            maxPro=Math.max(maxPro,rightMax[i]-prices[i]);
        }
        return maxPro;
    }
}
