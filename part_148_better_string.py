def solve(  str1: str, ans: set, idx: int, temp: str):
        # Base case: If we've traversed the entire string, add the subsequence to the set
        if idx >= len(str1):
            ans.add(temp)  # Use a set to automatically handle duplicates
            return

        # Recursive case: Exclude or include the current character
        solve(str1, ans, idx + 1, temp)
        solve(str1, ans, idx + 1, temp + str1[idx])
    
def generateSubSeq(  str1: str) -> int:
        idx = 0
        ans = set()  # Use a set to avoid duplicates
        temp = ""
        solve(str1, ans, idx, temp)
        return len(ans)


def betterString(  str1: str, str2: str) -> str:
        # Calculate the number of unique subsequences for both strings
        ans1 =  generateSubSeq(str1)
        ans2 =  generateSubSeq(str2)
    
        # Return the string with more unique subsequences
        return str1 if ans1 >= ans2 else str2
