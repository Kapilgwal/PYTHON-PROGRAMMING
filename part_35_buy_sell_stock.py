def maxProfit(price : list[int]) -> int:
    mini = 1e9
    profit = 0
    
    for i in range(len(price)):
        mini = min(mini,price[i])
        profit = max(profit,price[i] - mini)
    
    return profit 

def main():
    price = [7,1,5,3,6,4]
    ans = maxProfit(price)
    print(ans)

if __name__ == "__main__":
    main()