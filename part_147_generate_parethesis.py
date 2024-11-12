def isValid(temp: list[str]):
    st = []

    for i in temp:
        if i == "(":
            st.push(i)

        else:
            if len(st) == 0:
                return False
            st.pop()

    return len(st) == 0


def solve(temp: list[str], ans: list[str], open : int,close : int,n : int):

    if len(temp) == 2*n:
        ans.append("".join(temp))
        return 
    
    if open < n:
        temp.append("(")
        solve(temp,ans,open+1,close,n)
        temp.pop()
        
    if close < open:
        temp.append(")")
        solve(temp,ans,open,close+1,n)
        temp.pop()
        

def generateParenthesis(n: int):
    temp = []
    ans = []
    solve(temp,ans,0,0,n)
    return ans


def main():
    n = 3
    ans = generateParenthesis(n)
    print(ans)


if __name__ == "__main__":
    main()
