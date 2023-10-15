class Solution {
    public boolean isSubsequence(String s, String t) {
        char temp1[]=s.toCharArray();
        char temp2[]=t.toCharArray();
        int i=0,j=0;
        while(i<temp1.length&&j<temp2.length){
            if(temp1[i]==temp2[j]){
                i++;
                j++;
            }
            else{
                j++;
            }
        }
        return i==temp1.length;   
    }
}
