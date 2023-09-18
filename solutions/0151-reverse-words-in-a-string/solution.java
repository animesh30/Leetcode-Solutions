class Solution {
    public String reverseWords(String s) {
        s=s.trim();
        s=s.replaceAll("\\s+"," ");
        String temp[]=s.split(" ");
        String ans="";
        for(int i=temp.length-1;i>0;i--){
            ans+=temp[i]+" ";
        }
        ans+=temp[0];
        return ans;
    }
}
