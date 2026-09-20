# Week 10 Labwork - Factorial using Recursion
# Rafi Miazi (K250249)

import time

def factorial(n):
  
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    start = time.time()
    
    # Test values
    test_numbers = [0, 1, 5, 7, 12, 23]
    
    print("--- Factorial Calculation Results ---")
    for num in test_numbers:
        result = factorial(num)
        print(f"Factorial of {num} ({num}!) = {result}")
        
    end = time.time()
    print("\nExecution time:", end - start, "seconds")

if __name__ == '__main__':
    main()