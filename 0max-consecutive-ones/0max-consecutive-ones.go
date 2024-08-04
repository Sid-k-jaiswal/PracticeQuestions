func findMaxConsecutiveOnes(nums []int) int {
    
// [1,1,0,1,1,1] --> 3
// [1,0] --> 1
// [0,0,1,0,0] --> 1
// [0] --> 0
// [0,1] --> 1
    
    max := 0
    count := 0
    
    for i := 0; i < len(nums); i ++ {
        if nums[i] == 1 {
            count ++
        } else {
            count = 0
        }
        
        if count > max {
            max = count
        }
    }
    
    return max
}