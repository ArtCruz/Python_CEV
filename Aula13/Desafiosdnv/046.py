from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
    if c == 0:
        print('POW!POW!BOOM!')
