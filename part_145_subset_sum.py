def solve(ans: list[int], idx: int, current_sum: int, candidates: list[int]):
    # Base case: if we have reached the end of the array, add the current_sum to the ans list
    if idx >= len(candidates):
        ans.append(current_sum)
        return

    # Include the current candidate
    solve(ans, idx + 1, current_sum + candidates[idx], candidates)

    # Exclude the current candidate and move to the next
    solve(ans, idx + 1, current_sum, candidates)

def subsetSums(candidates: list[int]) -> list[int]:
    ans = []
    solve(ans, 0, 0, candidates)
    # Remove duplicates from the result and return sorted unique sums
    return sorted(list(set(ans)))

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    ans = subsetSums(candidates)
    print(ans)

if __name__ == "__main__":
    main()
