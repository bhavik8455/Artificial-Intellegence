tile1 = input("Enter the status of LEFT tile (DIRTY/CLEAN) : ")
tile2 = input("Enter the status of RIGHT tile (DIRTY/CLEAN) : ")
status = input("Enter the position of vaccum cleaner(LEFT/RIGHT) : ")

if status == 'LEFT':
    if tile1 == 'DIRTY':
        print("sucking and moving to right")
        
        if tile2 == 'DIRTY':
            print("sucking....")
            print("rest")
        else :
            print("rest")
    else:
        print("moving to right")
        if tile2 == 'DIRTY':
            print("sucking....")
            print("rest")
        else :
            print("rest")
else :
    if tile2 == 'DIRTY':
        print("sucking and moving to left")
        if tile1 == 'DIRTY':
            print("sucking....")
            print("rest")
        else :
            print("rest")
    else:
        print("moving to LEFT")
        
        if tile1 == 'DIRTY':
            print("sucking....")
            print("rest")
        else :
            print("rest")

    