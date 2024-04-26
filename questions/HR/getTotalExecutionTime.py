'''
when multiple tasks are executed on a
single-threaded CPU, the tasks are
scheduled based on the principle of pre-emption. 
When a higher-priority task arrives
in the execution queue, then the lower-
priority task is pre-empted, i.e. its execution
is paused until the higher-priority task is
complete.

There are n functions to be executed on a
single-threaded CPU, with each function
having a unique ID between O and n-1.
Given an integer n, representing the
number of functions to be executed, and an
execution log as an array of strings, logs, of
size m. determine the exclusive times of
each of the functions. Exclusive time iS the
sum of execution times for all calls to a
'''

'''
To solve this problem in Python, we can use a stack to keep track of the function calls and their execution times. We'll iterate through the execution logs and update the exclusive time for each function accordingly.

In this code:

    We initialize a list exclusive_times to store the exclusive times for each function. The size of the list is n, where n is the number of functions.
    We initialize an empty stack to keep track of function calls.
    We iterate through each log in the logs array.
    For each log, we split it into function ID (fid), action (start or end), and time.
    If the action is start, we update the exclusive time for the function at the top of the stack (if any) and push the current function ID onto the stack.
    If the action is end, we pop the top function ID from the stack, update its exclusive time, and adjust the previous time accordingly.
    Finally, we return the list exclusive_times containing the exclusive times for each function.

time complexity is O(m), where m is the number of logs.
space complexity is O(n), where n is the number of functions.

'''
def exclusive_time(n, logs):
    exclusive_times = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        fid, action, time = log.split(':')
        fid = int(fid)
        time = int(time)

        if action == 'start':
            if stack:
                exclusive_times[stack[-1]] += time - prev_time
            stack.append(fid)
            prev_time = time
        else:
            exclusive_times[stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return exclusive_times

# Example usage:
n = 3
logs = ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:6","0:end:7"]
result = exclusive_time(n, logs)
print(result)  # Output: [3, 4, 1]

