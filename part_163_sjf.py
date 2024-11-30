def shortest_job_first(jobs):
    jobs.sort()

    wait_time = 0
    total_time = 0
    n = len(jobs)

    for i in range(n):

        wait_time += total_time

        total_time += jobs[i]

    return wait_time / n

if __name__ == "__main__":
    jobs = [4, 3, 7, 1, 2]

    print("Array Representing Job Durations:", end=" ")
    for job in jobs:
        print(job, end=" ")
    print()

    ans = shortest_job_first(jobs)
    print("Average waiting time:", ans)
                           
                        