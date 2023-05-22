from time import sleep


def prin():
    print('- ', end='')
    sleep(0.1)
    print('\b\\ ', end='')
    sleep(0.1)
    print('\b| ', end='')
    sleep(0.1)
    print('\b/ ', end='')
    sleep(0.1)

for i in range(100):
    print('- ', end='')
    sleep(0.1)
    print('\b\\ ', end='')
    sleep(0.1)
    print('\b| ', end='')
    sleep(0.1)
    print('\b/ ', end='')
    sleep(0.1)