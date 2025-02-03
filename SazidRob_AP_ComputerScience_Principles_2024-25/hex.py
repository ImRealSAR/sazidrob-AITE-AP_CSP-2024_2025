def hex_convert(n):
    res1 = n // 16
    res2 = n % 16
    nums = [10, 11, 12, 13, 14, 15]
    letts = ["A", "B", "C", "D", "E", "F"]
    for i in range(len(nums)):
        if res2 == nums[i]:
            res2 = letts[i]
        if res2 == nums[i]:
            res2 = letts[i]
        final_hex_code= str(res1) + str(res2)
        if final_hex_code[0] == "0":
            final_hex_code = final_hex_code[1:]
        final_hex_code = str(res1) + str(res2)
        print(final_hex_code)

hex_convert(255)

def dec_convert(n):
    powers_of_16 = []
    while n > 0:
        res = n % 16
        n = n // 16
        powers_of_16.append(res)
    powers_of_16.reverse()

