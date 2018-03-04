# Implement pow(x, n) % d.
# 
# In other words, given x, n and d

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return (1 % d)
        if n == 1:
            return (x % d)
        value = self.pow(x,int(n/2), d)
        if (n % 2) == 0:
            return ((value % d) * (value % d)) % d
        else:
            if n > 0:
                return ((x % d) * (value % d) * (value % d)) % d
            else:
                return ((value % d) * (value % d)/x) % d
