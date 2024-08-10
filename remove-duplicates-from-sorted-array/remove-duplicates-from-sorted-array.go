func removeDuplicates(nums []int) int {
    
    unique := 1
    
    for i:=1; i < len(nums); i++ {
        
        if nums[i-1] != nums[i] {
            nums[unique] = nums[i]
            unique ++
        }
        
    }
    
    return unique
    
// 2nd ...
    
//     unique := 0
    
//     for i:=1; i < len(nums); i++ {
//         if nums[i] != nums[unique] {
//             unique ++
//             nums[unique] = nums[i]
//         }
//     }
    
//     return unique + 1
    
}