def input_decimal():
    """输入十进制数（带验证）"""
    while True:
        try:
            num = int(input("请输入十进制数: "))
            if num >= 0:
                return num
            else:
                print("请输入非负数！")
        except ValueError:
            print("请输入有效的数字！")

def input_binary():
    """输入二进制数（带验证）"""
    while True:
        binary = input("请输入二进制数: ")
        if all(c in "01" for c in binary):
            return binary
        else:
            print("二进制数只能包含0和1！")

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
