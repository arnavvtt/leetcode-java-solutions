class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result= new ArrayList<>();
        ArrayList<Integer> current = new ArrayList<>();

        solve(0,nums,result,current);
        return result ;
        
    }
    void solve(int i,int[] nums,List<List<Integer>> result,ArrayList<Integer> current){
        if(i==nums.length){
            result.add(new ArrayList<>(current));
            return;
        }
        current.add(nums[i]);// here we are adding the integers in the current named ArrayList
        solve(i+1,nums,result,current);

        current.remove(current.size()-1);// here we are doing the backtrack and removing the nums for example after adding complete [1,2,3] we do backtrack and remove 3

        solve(i+1,nums,result,current); // now we do have the option after backtracking wheter to choose or not in skip step we wil follow this i.e not add but move i+1)


    }

    

}