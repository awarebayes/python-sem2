def bin_add_one(bin_str):
    carry_over = True
    res = []
    for i in reversed(bin_str):
        if carry_over:
            if i == "1":
                res.append("0")
            if i == "0":
                res.append("1")
                carry_over = False
        else:
            res.append(i)
    return "".join(reversed(res))


invert_bin = {"1": "0", "0": "1"}.get

# my bin function
def my_bin(dec_str):
    num = int(dec_str)
    assert -127 < num < 127
    res = ["0" for _ in range(8)]
    if num > 0:
        for i in range(8):
            if num % 2 != 0:
                res[i] = "1"
            num //= 2
    else:
        inversed = my_bin(str(-num))
        inverted = "".join(map(invert_bin, inversed))
        print("inverted", inverted)
        one_added = bin_add_one(inverted)
        print("one_added", one_added)
        return one_added[:8]

    return "".join(reversed(res))


# my int function
def my_int(bin_str, ignore_first=False):
    if bin_str[0] == "1" and not ignore_first:
        return my_int(bin_add_one("".join(map(invert_bin, bin_str[1:]))), True)
    res = 0
    cur_pow = 1
    for i in reversed(bin_str):
        if i == "1":
            res += cur_pow
        cur_pow *= 2
    return str(res)


b = my_bin("-6")
print(b)
i = my_int(b)
print(i)
