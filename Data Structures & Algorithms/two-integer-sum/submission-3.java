class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> m1=new HashMap<>();
        for (int i=0;i< nums.length;i++){
            int ans=target-nums[i];
            if(m1.containsKey(ans)){
                return new int[]{m1.get(ans),i};
            }
            m1.put(nums[i],i);
        }
        return new int[]{};
    }
}
