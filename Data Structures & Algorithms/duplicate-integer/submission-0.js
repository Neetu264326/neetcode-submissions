class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
       // return new set(nums).size !==nums.length;
       let map={};
       for(let i=0;i<nums.length;i++){
        if(map.hasOwnProperty(nums[i])){
            return true ;
        }
        map[nums[i]]=1;
       }
       return false;
    }
}
