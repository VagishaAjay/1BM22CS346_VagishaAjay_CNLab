def crc8(data):
    n = len(data)
    data = '0b' + data  # Convert to binary format in Python
    word = int(data, 2)  # Convert binary string to an integer
    div = 139  # CRC-8 divisor (10001011 in binary)
    word <<= 7  # Left shift by 7 bits (add 7 zeroes)
    check = 1 << (n + 7 - 1)  # Bit to check the first digit (MSB)
    div <<= (n - 1)  # Align the divisor with the input data length
    res = word
    for i in range(n):
        # XOR if the current bit is 1
        if res & check:
            res = res ^ div
        div >>= 1
        check >>= 1  # Shift check bit to handle dropped leftmost bit
    return word ^ res  # Return the CRC remainder


def checkCrc(codeword):
    n = len(codeword)
    word = int(codeword, 2)
    div = 139  # CRC-8 divisor (10001011 in binary)
    check = 1 << (n - 1)  # Bit to check the first digit (MSB)
    div <<= (n - 8)  # Align the divisor with the input codeword length
    res = word
    for i in range(n - 7):  # Process only the dataword part
        if res & check:
            res = res ^ div
        div >>= 1
        check >>= 1
    return res == 0  # If remainder is 0, no error


# Main function
data = input("Enter the binary number for CRC-8: ")
codeword = bin(crc8(data))[2:]  # Generate codeword
print('Codeword using crc8:', codeword)

new_codeword = input("Enter codeword for CRC checking: ")
print('No errors in data check') if checkCrc(new_codeword) else print('Error in data check')
