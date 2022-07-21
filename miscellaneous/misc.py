def dot_product_bit_strings(string1: str, string2: str):
    # TODO: Add sanity check for binary string
    result = 0
    for i in range(len(string1)):
        result += int(string1[i]) * int(string2[i])
    return result % 2
