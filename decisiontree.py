i0 = input("Are you a WUT student already? y/n: " )
i1s = input("Do you have polish citizenship? y/n: ")
i2 = input("Are a phd in the making? y/n: " )
i3 = input("Do you intend to study on WUT? y/n: " )
i4 = input("I-st degree? y/n: ")
i5 = input("Are you going to study full time? y/n: ")
i6 = input("Are you an erasmus student? y/n: " )

print(i0)

# Jak chcesz żeby działało to daj
# While True: przed każdym warunkiem
# i będzie cacy... :3

while True:
    if i0 == "y":
       i1s
       while True:
            if i1s == "y":
                print("Current Polish Students - April")
                break
            else:
                print("Current Foreign Students - April")
                break
    else:
        i2
        if i2 == "y":
            print("PHD - April")
            break
        else:
            i1s
            while True:
                if i1s == "y":
                    i3
                    if i3 == "y":
                        i4
                        if i4 == "y":
                            print("new candidates - july")
                            break
                        else:
                            print("II or IIIrd deg - september")
                            break
                    else:
                        print("Learn about Bank of Rooms")
                        break
            else:
                i5
                if i5 == "y":
                    print("new international students - august")
                    break
                else:
                    i6
                    if i6 == "y":
                        print("erasmus students - july")
                        break
                    else:
                        print("Bilateral exchange - june")
                        break
