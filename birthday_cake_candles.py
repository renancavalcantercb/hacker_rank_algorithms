def birthday_cake_candles(n, ar):
    max_height = max(ar)
    print(max_height)
    print(ar.count(max_height))
    return ar.count(max_height)
