func runningSum(nums []int) []int {
    
    var sum = []int{nums[0]}
    
    for i := 1; i < len(nums); i++ {
        sum = append(sum,sum[i-1]+nums[i])
    }
    
    return sum
    
}