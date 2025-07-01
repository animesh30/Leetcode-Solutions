class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer> indexMap = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char currChar = s.charAt(i);
            int totalOccurence = indexMap.getOrDefault(currChar,0);
            totalOccurence++;
            indexMap.put(currChar,totalOccurence);
        }
        for(int i=0;i<s.length();i++){
            char currChar = s.charAt(i);
            if(indexMap.get(currChar)==1){
                return i;
            }
        }
        return -1;
    }
}
