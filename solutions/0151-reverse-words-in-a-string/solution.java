class Solution {
    public String reverseWords(String s) {
        s=s.replaceAll("\\s+"," ").trim();
        s=s+" ";
        String revStr = new String();
        String tempStr = new String();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==' '){
                revStr = tempStr+" "+revStr;
                tempStr="";
            }
            else{
                tempStr=tempStr+s.charAt(i);
            }
        }
        revStr=revStr.trim();
        return revStr;
    }
}
