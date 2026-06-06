class Solution {
    public int[] getConcatenation(int[] nums) {
        int ans = nums.length;
        int []n=new int [2*ans];
        for(int i=0;i<ans;i++){
            n[i]=nums[i];
            n[i+ans]=nums[i];
        }
          return n;
    }
  
}