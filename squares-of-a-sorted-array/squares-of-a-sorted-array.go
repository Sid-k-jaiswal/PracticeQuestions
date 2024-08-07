func sortedSquares(nums []int) []int {
    
    i := 0
    j := len(nums)-1
    x := len(nums)-1
    
    result := make([]int,len(nums))
    
    for i <= j {
        
        sq1 := nums[i]*nums[i]
        sq2 := nums[j]*nums[j]
        
        if sq1 > sq2 {
            result[x] = sq1
            x --
            i++
        } else {
            result[x] = sq2
            x --
            j --
        }
    }
    
    return result
}