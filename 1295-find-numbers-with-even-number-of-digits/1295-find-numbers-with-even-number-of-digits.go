func findNumbers(nums []int) int {
    
    total := 0
    
    for i:= 0; i < len(nums); i++ {
        
        even := 0
        
        for nums[i] > 0 {
            nums[i] = nums[i]/10
            even ++
        }
        
        if even % 2 == 0 {
            total ++
        }
        
    }
    
    return total
    
}