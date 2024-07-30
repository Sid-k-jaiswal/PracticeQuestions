class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        output = 0
        
        for i in range(len(accounts)):
            wealth = 0
            
            for j in range(len(accounts[0])):
                wealth = wealth + accounts[i][j]
                
            if wealth > output:
                output = wealth
        
        return output
        
            
        