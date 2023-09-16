class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char temp[]=magazine.toCharArray();
        HashMap<Character, Integer> map=new HashMap<>();
        for(int i=0;i<temp.length;i++){
            int value=0;
            if(map.containsKey(temp[i])){
                value = map.get(temp[i]);
            }
            value++;
            map.put(temp[i],value);
        }
        char s2[] = ransomNote.toCharArray();
        for(int i=0;i<s2.length;i++){
            if(map.containsKey(s2[i])){
                int value = map.get(s2[i]);
                value--;
                if(value>0){
                    map.put(s2[i],value);
                }
                else{
                    map.remove(s2[i]);
                }
            }
            else{
                return false;
            }
        }
        return true;
    }
}
