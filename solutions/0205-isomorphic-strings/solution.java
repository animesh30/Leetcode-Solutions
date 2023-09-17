class Solution {
    public boolean isIsomorphic(String s, String t) {
        char temp1[]=s.toCharArray();
        char temp2[]=t.toCharArray();
        HashMap<Character,Character> map= new HashMap<>();
        for(int i=0;i<temp1.length;i++){
            if(map.containsKey(temp1[i])){
                if(map.get(temp1[i])!=temp2[i]){
                    return false;
                }
            }
            else{
                map.put(temp1[i],temp2[i]);
            }
        }
        map.clear();
        for(int i=0;i<temp1.length;i++){
            if(map.containsKey(temp2[i])){
                if(map.get(temp2[i])!=temp1[i]){
                    return false;
                }
            }
            else{
                map.put(temp2[i],temp1[i]);
            }
        }
        return true;
    }
}
