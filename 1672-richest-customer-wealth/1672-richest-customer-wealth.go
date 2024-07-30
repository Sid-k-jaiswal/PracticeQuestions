func maximumWealth(accounts [][]int) int {
    
    // wealth := 0
    
//     for i := 0; i < len(accounts); i++ {
//         sum := 0
//         for j := 0; j < len(accounts[0]); j++ {
//             sum += accounts[i][j]
//         }
//         if sum > wealth {
//             wealth = sum
//         }
//     }
    
//     return wealth
    
   // 2nd ...
    
    wealth := 0
    
    for _, j := range accounts{
        sum := 0
        for _,l := range j {
            sum += l
        }
        
        if sum > wealth {
            wealth = sum
        }
    }
    
    return wealth
}