def LemonadeChange(bills : list[int]) -> bool:
    
    five = 0
    ten = 0
    
    for i in bills:
        
        if i == 5:
            five += 1
        
        elif i==10:
            if five > 0:
                ten += 1
                five -= 1
            
            else:
                return False
        else:
            
            if (ten > 0 and five > 0):
                ten -= 1
                five -= 1
            
            elif (five >= 3):
                five -= 3
            
            else:
                return False 
    
    return True
                

def main():
    bills = [5,5,10,10,20]
    ans = LemonadeChange(bills)
    print(ans)
    
if __name__ == "__main__":
    main()