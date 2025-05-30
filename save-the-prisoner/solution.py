def saveThePrisoner(n, m, s):
    # Write your code here
    final_seat = (s + (m - 1))
    if final_seat % n == 0:
        final_seat = n
    else:
        final_seat %= n
    return final_seat
