def decimalToBinary(num):
    binary = list()
    while num > 0:
        lastbit = num & 1
        num >>= 1
        binary.append(str(lastbit))
    return "".join(binary[::-1])


if __name__ == "__main__":
    num = int(input("Enter the number : "))
    ans = decimalToBinary(num)
    print(ans)

# output:

# Enter the number : 123456789
# 111010110111100110100010101