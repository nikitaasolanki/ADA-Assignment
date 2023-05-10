def make_change(denomination_list, amount):

    denomination_list.sort()
    n = len(denomination_list)
    i = n - 1
    ans = 0
    x = 0
    while i>= 0 :
        while denomination_list[i]<= amount:
            ans = +1
            amount -= denomination_list[i]
            i -= 1
        if amount == 0:
            x = 1
        elif amount<0:
            x = -1
    return x

    amount= 20
    denomination_list = [1,15,10]
    print(make_change(denomination_list, amount))
