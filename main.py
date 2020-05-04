def bin_to_gray(bin_list):
    b = [bin_list[0]]
    for i in range(1, len(bin_list)):
        b.append(bin_list[i] ^ bin_list[i - 1])
    return b


def gray_to_bin(bin_list):
    b = [bin_list[0]]
    for i in range(1, len(bin_list)):
        b.append(1 if b[i - 1] != bin_list[i] else 0)
    return b


def int_to_bin(x):
    arr = []
    for i in range(32):
        arr.append(x >> i & 1)
    arr.reverse()
    return arr


def bin_to_int(list_bin):
    x = 0
    for i in range(len(list_bin)):
        x += list_bin[i] * 2 ** (len(list_bin) - i - 1)
    return x


number = 573
print("number before operations = " + str(number))
print("int_num =  " + str(int_to_bin(number)))
print("gray_num = " + str(bin_to_gray(int_to_bin(number))))
print("bin_num =  " + str(gray_to_bin(bin_to_gray(int_to_bin(number)))))
print("number after operations = " + str(bin_to_int(gray_to_bin(bin_to_gray(int_to_bin(number))))))
