print("Amount Due: 50")
Amount_Due = 50
while(Amount_Due > 0):
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10  or coin == 5 :
            Amount_Due = Amount_Due - coin
            if 0 >= Amount_Due:
                print(f"Change Owed: {-1 * Amount_Due}")
            else:
                print(f"Amount Due: {Amount_Due}")

    else:
        print(f"Amount Due: {Amount_Due}")