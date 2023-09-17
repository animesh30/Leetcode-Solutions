class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char temp[]=s.toCharArray();
        for(int i=0;i<temp.length;i++){
            if(temp[i]=='('||temp[i]=='{'||temp[i]=='['){
                stack.push(temp[i]);
            }
            else{
                if(stack.size()==0){
                    return false;
                }
                else{
                    char ch=stack.pop();
                    if((temp[i]==')'&&ch!='(')||(temp[i]=='}'&&ch!='{')||(temp[i]==']'&&ch!='[')){
                        return false;
                    }
                }
            }
        }
        return stack.size()==0;
    }
}
