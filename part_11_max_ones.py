def main():
    arr = [1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1]
    
    maxCount = 0
    cnt = 0
    for i in arr:
        if i == 1:
            cnt += 1
        else:
            maxCount = max(maxCount,cnt)
            cnt = 0
    
    maxCount = max(cnt,maxCount)
    print(maxCount)
    
if __name__ == "__main__":
    main()        