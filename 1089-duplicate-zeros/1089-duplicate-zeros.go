func duplicateZeros(arr []int)  {
    
    zeroesCount := 0
    
    for i:=0; i < len(arr); i++ {
        if arr[i] == 0 {
            zeroesCount ++
        }
    }
        
    n := len(arr)
    
    for j:= n-1; j > -1; j -- {
        
        if zeroesCount + j < n {
            arr[zeroesCount + j] = arr[j] //shift the existing elements to right based on 0 count
        }
        
        if arr[j] == 0 {
            
            zeroesCount --
            
            if zeroesCount + j < n {
                arr[zeroesCount + j] = 0 // put 0 after the 0th element
            }
        }
    }
    
//         zeroesCount := 0
//         n := len(arr)

//         // Count the number of zeros
//         for i := 0; i < n; i++ {
//             if arr[i] == 0 {
//                 zeroesCount++
//             }
//         }

//         // Shift elements and duplicate zeros
//         for j := n-1; j >= 0; j-- {
//             // If there's enough space to place the element after shifting
//             if j + zeroesCount < n {
//                 arr[j + zeroesCount] = arr[j]
//             }

//             // If the element is zero, duplicate it
//             if arr[j] == 0 {
//                 zeroesCount--
//                 if j + zeroesCount < n {
//                     arr[j + zeroesCount] = 0
//                 }
//             }
//         }

// 2nd ...
    
//     for i:=0; i < len(arr); i++ {
//         if arr[i] == 0 {
            
//             for j:= len(arr)-1; j > i; j --{
//                 arr[j] = arr[j-1]
//             }
            
//             i ++
//         }
//     }
}