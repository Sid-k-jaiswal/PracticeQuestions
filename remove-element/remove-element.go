func removeElement(nums []int, val int) int {
    
    count := 0
    
    for _,i := range nums {
        
        if i != val {
            nums[count] = i
            count ++
        }
    }
    
    return count
}