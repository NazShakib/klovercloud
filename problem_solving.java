class Solution{
    public int solution(int X,int []A){
        int current_steps = X;
        boolean[] is_exits = new boolean[current_steps+1];
        for(int i = 0; i < A.length; i++){
            if(!is_exits[A[i]]){
                is_exits[A[i]] = true;
                current_steps--;
                if(current_steps == 0) {return i;}
            }

        }
        return -1;
    }
}

class Main
{
	public static void main(String[] args) {
	  
	  // testin cases
	  //{1,3,1,4,2,3,5,4}, X=5
	  //{4,5,7,6,7,4,5,2,1,3,7,5}, X= 7
	  //{4,1,6,4,3,2,1,4,5}, X= 6
	  int [] array = {4,5,7,6,7,4,5,2,1,3,7,5};
	  int X = 7;
	  Solution object = new Solution();
	  int result = object.solution(X,array);
	  System.out.println(result+1);
	}
    
}