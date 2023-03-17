def setBitsToZero():
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
    x = 119
    i = 2
    j = 4

    m1 = (~0) << (j + 1)
    m2 = 2**i -1
    mask = m1 | m2
    ans = x & mask

    return ans



print(setBitsToZero())