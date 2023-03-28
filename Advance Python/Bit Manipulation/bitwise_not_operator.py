"""
    NOT operation : ~

    How numbers are stored in binary format?
        sign bit : 0 -> +ve and 1 -> -ve
    Now,
        ~x == -x-1

        1's complement → flipping of bits means chaanged the sign
        2's complement → add 1 to 1's complement

    case 1: x is +ve
        
        eg. x = 13 and ~x = -14

        step 1: 1's complement → flipping of bits
                0 | 1 1 0 1  == 13
                -----------
                1 | 0 0 1 0  == 2

        step 2: 2's complement → add 1 to 1's complement
                a -ve number stored as 2's complement

                0 0 1 0
                1 1 0 1  ← 1's complement
            +         1
            -----------
                1 1 1 0  ← It is 14

                Here, sign bit is 1 so it's a negative value
                
                so ~13 is -14.

    case 2: x is -ve
        x = -13

             0 | 1 1 0 1     ← binary of 13
             1 | 0 0 1 0     ← 1's complement
            +          1
            ------------
             1 | 0 0 1 1     ← binary of -13
             0 | 1 1 0 0     ← 1's complement of -13

             So ans is 1100 i.e. 12
            
            step 1: add 1 to -ve number
            step 2: remove the sign
"""

x = 13
print(~x)

x = -13
print(~x)

# output:

# -14
# 12