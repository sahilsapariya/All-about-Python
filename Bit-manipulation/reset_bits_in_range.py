def setBits(x, i, j):
    """
        binary of 119 is 1110111.
        1 1 1 0 1 1 1
            ↑   ↑
           j=4 i=2

        let we want to make i = 2 to j = 4 digits to 1 i.e. [11 101 11 → 11 111 11]

        mask will be 00 111 00 and take (or) of mask and x.

        Q. How to generate mask?
            Count the number of bits to change.
                N = j - i + 1
                here, N = 4 - 2 + 1 → N = 3

            Now, 2 ** N i.e 2 ** 3 == 8 
                 binary of 8 is 1000
                 add -1 from 2 ** N

                 So, 7 in binary is 111

            Take left shift of 7 by i
            i.e.    7 << 2 == 11100
            
            mask = 11100
    """
    binary = bin(x).replace("0b", "")
    if i in range(len(binary)) and j in range(len(binary)) and i <= j:
        N = j - i + 1
        mask = (2 ** N - 1) << i
        ans = x | mask
        return ans
    else:
        return "range is not valid for given number"

def resetBits(x, i, j):
    """
        binary of 119 is 1110111.
        1 1 1 0 1 1 1
            ↑   ↑
           j=4 i=2

        let we want to make i = 2 to j = 4 digits to zero i.e. [11 101 11 → 11 000 11]

        mask will be 11 000 11 and take (and) of mask and x.

        Q. How to generate mask?
            take the (or) of 11 00000 and 00000 11
            i.e.    11 000 00
                  + 00 000 11
                -------------
                    11 000 11  == mask
    """
    binary = bin(x).replace("0b", "")
    if i in range(len(binary)) and j in range(len(binary)) and i <= j:
        m1 = (~0) << (j + 1)
        m2 = 2**i -1
        mask = m1 | m2
        ans = x & mask
        return ans
    else:
        return "range is not valid for given number"


if __name__ == "__main__":
    num = int(input("Enter the number : "))
    i, j = map(int, input("Enter the i and j : ").split())

    x = resetBits(num, i, j)    
    print(x)

    x = setBits(num, i, j)
    print(x)