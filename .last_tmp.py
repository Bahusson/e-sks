i1 = input("Are you a WUT student already? y/n: " )
i2s = input("Do you have polish citizenship? y/n: ")
i3 = input("Are a phd in the making? y/n: " )
i4 = input("Do you intend to study on WUT? y/n: " )
i5 = input("I-st degree? y/n: ")
i6 = input("Are you going to study full time? y/n: ")
i7 = input("Are you an erasmus student? y/n: " )
i8

print(i1)

while True:
    if i1 == "y":
       i2s
       while True: 
            if i2s == "y":
                print("Current Polish Students - April")
                break
            else:
                print("Current Foreign Students - April")
                break
    else:
        i3
        if i3 == "y":
            print("PHD - April")
            break         
        else:
            i2s
            while True:
                if i2s == "y":
                    i4
                    if i4 == "y":
                        i5
                        if i5 == "y":
                            print("new candidates - july")
                            break
                        else:
                            print("II or IIIrd deg - september")
                            break
                    else:        
                        print("Learn about Bank of Rooms")
                        break
            else:
                i6
                if i6 == "y":
                    print("new international students - august")
                    break
                else:
                    i7
                    if i7 == "y":
                        print("erasmus students - july")
                        break
                    else:
                        print("Bilateral exchange - june")