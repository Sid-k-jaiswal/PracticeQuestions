func canConstruct(ransomNote string, magazine string) bool {
    
    if len(ransomNote) > len(magazine) {
        return false
    }
    
    output := make(map[rune]int)
    
    for _,c := range magazine {
        output[c] ++
    }
    
    for _,c := range ransomNote {
        
        if output[c] == 0 {
            return false
        }
        
        output[c] --
    }
    
    return true

// 2nd ...
    
//     if len(ransomNote) > len(magazine) {
//         return false
//     }
    
//     list := [26]int{}
    
//     for _, character := range magazine {
//         list[character - 'a'] ++
//     }
    
//     for _, character := range ransomNote {
//         if list[character - 'a'] == 0 {
//             return false
//         }
        
//         list[character - 'a'] --
//     }
    
//     return true
}