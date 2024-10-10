
def mergeIntervals(intervals : list[list[int]]) -> list[list[int]]:
    # Sort the intervals based on the start times
    intervals.sort()
    
    # Resultant list to store merged intervals
    ans = []
    
    # Initialize with the first interval
    ans.append(intervals[0])
    
    # Iterate through the sorted intervals
    for i in range(1, len(intervals)):
        # Get the last interval's end time in ans
        last_interval = ans[-1]
        current_start = intervals[i][0]
        current_end = intervals[i][1]
        
        # If there's an overlap, merge the intervals
        if last_interval[1] >= current_start:
            # Update the end time of the last interval in ans
            ans[-1][1] = max(last_interval[1], current_end)
        else:
            # No overlap, add the current interval to the result list
            ans.append(intervals[i])
    
    return ans

def main():
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    ans = mergeIntervals(intervals)
    print(ans)


if __name__ == "__main__":
    main()