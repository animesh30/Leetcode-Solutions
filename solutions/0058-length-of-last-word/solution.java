class Solution {
    public int lengthOfLastWord(String s) {
        s=s.trim();
        int i=s.length()-1,count=0;
        while(i>=0&&s.charAt(i)!=' '){
            i--;
            count++;
        }
        return count;
    }
}
