i1 = input("Are you a WUT student already? y/n: " )
i2s = input("Do you have polish citizenship? y/n: ")
i3 = input("Are a phd in the making? y/n: " )
i4 = input("Do you intend to study on WUT? y/n: " )
i5 = input("I-st degree? y/n: ")
i6 = input("Are you going to study full time? y/n: ")
i7 = input("Are you an erasmus student? y/n: " )

print(i1)

if i1 == "y":
    i2s
    if i2s == "y":
        print("Current Polish Students - April")
    else:
        print("Current Foreign Students - April")
else:
    i3
    if i3 == "y":
        print("PHD - April")
    else:
        i2s
        if i2s == "y":
            i4
            if i4 == "y":
                i5
                if i5 == "y":
                    print("new candidates - july")
                else:
                    print("II or IIIrd deg - september")
            else:
                print("Learn about Bank of Rooms")
        else:
            i6
            if i6 == "y":
                print("new international students - august")
            else:
                i7
                if i7 == "y":
                    print("erasmus students - july")
                else:
                    print("Bilateral exchange - june")
