class knapsack:

    def __init__(self, size, capacity) -> None:
        self.size = size
        self.capacity = capacity
        self.items = []
        self.profit = []
        self.dp = [[0 for x in range(self.capacity + 1)] for x in range(self.size + 1)]
    
    def initializeArr(self):

        for i in range(self.size):
            print(f"Enter the item and it's profit respectively {i+1} : ", end='')
            s, m = map(int, input().split())
            self.items.append(s)
            self.profit.append(m)

    def printDP(self):

        print("This is the table dp")

        for i in range(self.size+1):
            for j in range(self.capacity+1):
                print(self.dp[i][j], end='\t')
            print('')

        print('')


    def knapsackdp(self):
        self.initializeArr()

        for i in range(1, self.size+1):
            for j in range(1, self.capacity+1):

                if j - self.items[i-1] >= 0:
                    self.dp[i][j] = max(self.dp[i-1][j], (self.profit[i-1] + self.dp[i - 1][j - self.items[i-1]]))
                else:
                    self.dp[i][j] = self.dp[i-1][j]
        self.printDP()


if __name__ == "__main__":
    size = int(input("Enter the number of items : "))
    capacity = int(input("Enter the capacity of bag : "))

    k = knapsack(size, capacity) 
    k.knapsackdp()