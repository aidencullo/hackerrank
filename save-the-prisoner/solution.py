def saveThePrisoner(n, m, s):
    final_seat = (s + (m - 1))
    return ((final_seat - 1) % n) + 1
