def dec_bin(n):
    final_res = ""
    while n > 0:
        res = n % 2
        n = n // 2
        final_res = str(res) + final_res
    print(final_res)

dec_bin(8)