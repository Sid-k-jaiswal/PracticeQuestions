The key insight here is that the running sum up to index i is the sum of nums[i] and the running sum up to index i-1.
​
###### Here is a more detailled explanation:
​
We know that
​
`sum[i] = nums[0] + nums[1] + ... + nums[i-1] + nums[i].`
​
###### So,
​
`sum[i-1] = nums[0] + nums[1] + ... + nums[i-1]`
​
so we can rewrite the first expression to get that
######
`sum[i] = sum[i-1] + nums[i]`
######
This code has a time complexity of O(N) since it only takes one pass, which will make the program run much faster when given a very large nums array. However, there is still a way to optimize the space we use.