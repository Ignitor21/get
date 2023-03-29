def binary2decimal(value):
    answer = 0
    for i in range(8):
        answer += value[i]*(2**(7 - i))

    return answer

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

a = decimal2binary(8)
print(a)
b = binary2decimal(a)
print(b)