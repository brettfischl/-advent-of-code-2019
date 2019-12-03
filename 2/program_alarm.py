

def main():
    op_codes = [
        1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0
    ]

    i = 0
    while i < len(op_codes):
        op_code = op_codes[i]
        if op_code == 1:
            op_codes = addition(op_codes, i)
        elif op_code == 2:
            op_codes = multiplication(op_codes, i)
        else:
            break
        i += 4
    return op_codes

def addition(op_codes, index):
    a, b = search(op_codes, index)
    op_codes[op_codes[index + 3]] = a + b
    return op_codes

def multiplication(op_codes, index):
    a, b = search(op_codes, index)
    op_codes[op_codes[index + 3]] = a * b
    return op_codes


def search(op_codes, index):
    a = op_codes[op_codes[index + 1]]
    b = op_codes[op_codes[index + 2]]
    return a, b

print(main())