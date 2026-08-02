import time

start_time = time.time()

for number in range(101):
    print(number)

end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time} seconds")