class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
            return false;
        int temp=x,revNum=0;
        while(temp>0){
            int dig=temp%10;
            revNum=(10*revNum)+dig;
            temp=temp/10;
        }
        return (x==revNum);
    }
}
