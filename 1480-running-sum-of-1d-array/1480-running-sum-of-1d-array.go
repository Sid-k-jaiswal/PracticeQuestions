func runningSum(nums []int) []int {
    
//     sum := []int{nums[0]}
//     length := len(nums)
    
//     for i := 1; i < length; i++ {
//         sum = append(sum, sum[i-1]+nums[i])
//     }
    
//     return sum
    
// 2nd ...
    
//     sum := make([]int, len(nums))
    
//     sum[0] = nums[0]
    
//     for i := 1; i < len(nums); i++ {
//         sum[i] = sum[i-1]+nums[i]
//     }
    
//     return sum

// 3rd ...
    
    for i := 1; i < len(nums); i++ {
        nums[i] += nums[i-1]
    }
    
    return nums
    
}