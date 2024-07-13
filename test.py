for i in range(8):
    print(i)
    for i in range(8):
        print("test")
        if i == 4:
            break
    for i in range(8):
        print("ERFOLG")