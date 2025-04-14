class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> valueMap = new HashMap<>();
        valueMap.put('I',1);
        valueMap.put('V',5);
        valueMap.put('X',10);
        valueMap.put('L',50);
        valueMap.put('C',100);
        valueMap.put('D',500);
        valueMap.put('M',1000);
        int ans=0;
        char ch[]=s.toCharArray();
        int length = ch.length;
        for(int i=0;i<length-1;i++){
            if(valueMap.get(ch[i])<valueMap.get(ch[i+1])){
                ans-=valueMap.get(ch[i]);
            }
            else{
                ans+=valueMap.get(ch[i]);
            }
        }
        ans+=valueMap.get(ch[length-1]);
        return ans;
    }
}
