jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
jobs.sort(key=lambda x: x[2], reverse=True)
n = len(jobs)
slots = [-1]*n
for job in jobs:
    for j in range(min(n, job[1])-1, -1, -1):
        if slots[j] == -1:
            slots[j] = job[0]
            break
print("Job sequence:", [j for j in slots if j != -1])