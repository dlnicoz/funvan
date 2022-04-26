# Job sequence
# Function to schedule the jobs

def printjobschedule(array, t):

    m = len(array)

    
    for j in range(m):
        for q in range(m - 1 - j):
            if array[q][2] < array[q + 1][2]:
                array[q], array[q + 1] = array[q + 1], array[q]

    res = [False] * t

   

    job = ['-1'] * t

    for q in range(len(array)):

        \

        for q in range(min(t - 1, array[q][1] - 1), -1, -1):

            if res[q] is False:
                res[q] = True
                job[q] = array[q][0]
                break


    print(job)




array = [['a', 7, 202],
       ['b', 5, 29],
       ['c', 6, 84],
       ['d', 1, 75],
       ['e', 2, 43]]

print("Maximum profit sequence of jobs is- ")
printjobschedule(array, 3)
