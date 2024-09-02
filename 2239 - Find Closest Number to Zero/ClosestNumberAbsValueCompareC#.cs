public class Solution {
    public int FindClosestNumber(int[] nums) =>
        List<int> numList = new List<int>();
        int closest = nums[0];
        numList.AddRange(nums);
        foreach (int num in numList) 
        {
            if (MathF.Abs(num) < MathF.Abs(closest))
            {
                closest = num;
            }
        }
        if (closest < 0 && numList.Contains((int)MathF.Abs(closest))) 
        {
            return (int)MathF.Abs(closest);
        }
        else
        {
            return closest;
        }
    }
}
