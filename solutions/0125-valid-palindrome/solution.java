class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        String temp = s.replaceAll("[^a-zA-Z0-9]","");
        int i=0,j=temp.length()-1;
        char ch[]=temp.toCharArray();
        while(i<j){
            if(ch[i]!=ch[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
