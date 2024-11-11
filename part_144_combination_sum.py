def solve(ans: list[list[int]], temp: list[int], idx: int, current_sum: int, candidates: list[int], target: int):
    if current_sum == target:
        ans.append(temp[:])  # Add a copy of temp to ans
        return
    if current_sum > target or idx >= len(candidates):
        return

    # Include the current candidate
    temp.append(candidates[idx])
    solve(ans, temp, idx + 1, current_sum + candidates[idx], candidates, target)
    temp.pop()  # Backtrack

    # Exclude the current candidate and move to the next
    solve(ans, temp, idx + 1, current_sum, candidates, target)

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    ans = []
    candidates.sort()  # Sort to handle duplicates
    solve(ans, [], 0, 0, candidates, target)
    # Remove duplicates from the result
    unique_ans = []
    for comb in ans:
        if comb not in unique_ans:
            unique_ans.append(comb)
    return unique_ans

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = combinationSum(candidates, target)
    print(ans)

if __name__ == "__main__":
    main()
