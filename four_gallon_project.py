def four_gallon_bucket ():
    three_gallon = 0
    five_gallon = 0

    # fill the 3 gallon (3,0)
    three_gallon = 3
    print(f"Fill the 3 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # pour from 3 gallon to 5 gallon (0,3)
    five_gallon += three_gallon
    three_gallon = 0
    print(f"Pour the 3 gallon bucket to 5 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # fill the 3 gallon (3,3)
    three_gallon = 3 
    print(f"Fill the 3 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # pour from 3 gallon to 5 gallon (1,5)
    # calculate the remain capacity in 5 gallon bucket 
    remaining_capacity = 5 - five_gallon
    #transfer from 3 gallon to 5 gallon
    if three_gallon <= remaining_capacity:
        five_gallon += three_gallon
        three_gallon = 0
    else:
        three_gallon -= remaining_capacity
        five_gallon = 5
        print(f"Pour the 3 gallon bucket to 5 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # empty the 5 gallon (1,0)
    five_gallon = 0
    print(f"Empty the 5 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # pour from 3 gallon to 5 gallon (0,1)
    five_gallon = three_gallon 
    three_gallon = 0
    print(f"Pour the 3 gallon bucket to 5 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # fill the 3  gallon (3,1)
    three_gallon = 3
    print(f"Fill the 3 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # pour 3 gallon into 5 gallon bucket (0,4)
    five_gallon += three_gallon
    print(f"Pour the 3 gallon bucket to 5 gallon bucket: (3-gallon: {three_gallon}, 5-gallon: {five_gallon})")

    # check if we have 4 gallon in 5 gallon bucket 
    if five_gallon == 4:
        print("Sucess")
    else:
        print("Failed")

four_gallon_bucket()