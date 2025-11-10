def count_down(n):
    while n >= 0:
        print(n)
        n -= 1   # Decrease n by 1 each time to avoid infinite loop

# Call the function
count_down(5)
