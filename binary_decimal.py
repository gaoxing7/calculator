def bin_to_dec(binary):
     decimal_num = 0
     for i, digit in enumerate(reversed(binary)):
         decimal_num += int(digit) * (2 ** i)
     return decimal_num

def dec_to_bin(num):
    bin_str = ''
    while num > 0:
        bin_str = str(num % 2) + bin_str
        num = num // 2
    return bin_str
