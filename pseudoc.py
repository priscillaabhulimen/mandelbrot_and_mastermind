MAX_ITER = 5000

c = complex(0, -1)
n = 0
z = 0

def escape_time():
    while n < MAX_ITER and abs(z) <= 2:
        z = z**2 + c
        n += 1

    return n



print(f'The value of z survived {escape_time} iterations.')