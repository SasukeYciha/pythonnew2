def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str