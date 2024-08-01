func numberOfSteps(num int) int {
    
    count := 0
    
    for num > 0 {
        if num%2 == 0 {
            num = num/2
        } else {
            num = num -1
        }
        
         count++
    }
    
    return count
}
    
// 2nd ...
    
//     if num == 0 {
//         return 0
//     }
    
//     if num%2 == 0 {
//         return 1 + numberOfSteps(num/2)
//     } else {
//         return 1 + numberOfSteps(num-1)
//     }
    
//     return num
    
//}