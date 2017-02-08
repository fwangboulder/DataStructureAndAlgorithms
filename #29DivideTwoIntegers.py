class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = 2147483647
        min_int = -2147483648
        if dividend == min_int and divisor == -1:
            return max_int
        signal = 1
        #positive or negative
        if dividend < 0:
            signal = -signal
        if divisor < 0:
            signal = -signal

        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        #19/3
        #dividend 12 times=4
        #7    6  times 2
        while dividend >= divisor:
            d, times = divisor, 1
            while d <= dividend:
                d <<= 1
                times <<= 1
                print d
                print times
            d >>= 1
            times >>= 1
            res += times
            dividend -= d
        return res * signal
