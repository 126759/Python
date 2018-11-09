import random

choice = int(input("Would you like an IPV4 (1), or IPV6(2)"))

if choice == 1:
    ipv4 = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    print(ipv4)

elif choice == 2:
    ipv6 = ".".join(map(str, (random.randint(0, 255) for i in range(6))))
    print(ipv6)
