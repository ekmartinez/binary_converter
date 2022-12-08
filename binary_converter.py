
class converter:
    """Converts binaries into decimals and vice versa"""

    def __init__(self, num):
        self.num = num

    def to_decimal(self):
        """From binary to decimal"""

        decimal = 0

        start = 1
        powers = [1]

        for x in range(len(self.num)-1):
            start *= 2
            powers.append(start)

        powers.reverse()

        for i, v in enumerate(str(self.num)):
            decimal += (int(v) * powers[i])
            
        return decimal

    def to_binary(self):                
        """From decimal to binary"""

        self.num = int(self.num)
        
        binary = ''
        bin_lst = []

        while self.num > 0:
            calc = divmod(self.num, 2)
            self.num = calc[0]
            bin_lst.append(calc[1])

        for b in reversed(bin_lst):
            binary += str(b)

        return binary

