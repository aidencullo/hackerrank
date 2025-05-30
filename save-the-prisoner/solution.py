def saveThePrisoner(n, m, s):
    # Write your code here
    final_seat = (s + (m - 1))
    while final_seat > n:
        final_seat -= n
    return final_seat
