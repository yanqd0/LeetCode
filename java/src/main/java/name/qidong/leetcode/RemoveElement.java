package name.qidong.leetcode;

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == val) ++count;
            else nums[i - count] = nums[i];
        }
        return nums.length - count;
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Element.
Memory Usage: 35.3 MB, less than 100.00% of Java online submissions for Remove Element.
*/
