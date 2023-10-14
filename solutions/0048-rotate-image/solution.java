class Solution {
    public void rotate(int[][] matrix) {
        int i=0,j=matrix.length-1;    
        while(i<j){
            int k=0;
            while(k<matrix.length){
                int temp=matrix[i][k];
                matrix[i][k]=matrix[j][k];
                matrix[j][k]=temp;
                k++;
            }
            j--;
            i++;
        }
        i=0;
        while(i<matrix.length){
            j=0;
            while(j<matrix.length){  
                if(j<=i){
                    
                }
                else{
                    int temp=matrix[i][j];
                    matrix[i][j]=matrix[j][i];
                    matrix[j][i]=temp;
                }
                j++;
            }
            i++;
        }
    }
}
