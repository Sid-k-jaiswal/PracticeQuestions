func maximumWealth(accounts [][]int) int {
    
    wealth := 0
    
    for i := 0; i < len(accounts); i++ {
        sum := 0
        for j := 0; j < len(accounts[0]); j++ {
            sum += accounts[i][j]
        }
        if sum > wealth {
            wealth = sum
        }
    }
    
    return wealth
}