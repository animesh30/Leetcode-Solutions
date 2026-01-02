class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        Map<Character,Integer> countMap1 = new HashMap<>();
        Map<Character,Integer> countMap2 = new HashMap<>();
        for(char c:s.toCharArray()){
            int occurence = countMap1.getOrDefault(c,0);
            countMap1.put(c,occurence+1);
        }
        for(char c:t.toCharArray()){
            int occurence = countMap2.getOrDefault(c,0);
            countMap2.put(c,occurence+1);
        }
        for(Map.Entry<Character,Integer> entry:countMap1.entrySet()){
            char currLetter = entry.getKey();
            int occ = countMap2.getOrDefault(currLetter,0);
            if(occ!=entry.getValue()){
                return false;
            }
        }
        return true;
    }
}
