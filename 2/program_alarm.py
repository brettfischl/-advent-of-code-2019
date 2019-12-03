op_codes = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0
]

def run_operation(program):
    i = 0
    result = program
    while i < len(result):
        op_code = result[i]
        a, b = search(result, i)
        if op_code == 1:
            result[result[i + 3]] = a + b
        elif op_code == 2:
            result[result[i + 3]] = a * b
        else:
            break
        i += 4
    return result


def search(program, index):
    a = program[program[index + 1]]
    b = program[program[index + 2]]
    return a, b

noun, verb = 0, 0
target = 19690720

while noun <= 99:
    solution = []
    program_codes = op_codes
    if op_codes[0] != 1:
        break
    while verb <= 99:
        if op_codes[0] != 1:
            break
        program_codes = op_codes.copy()
        program_codes[1] = noun
        program_codes[2] = verb
        solution = run_operation(program_codes)
        if solution[0] == target:
            print("SUCCESS")
            print(solution[0:3])
            print(100 * solution[1] + solution[2])
            break
        verb += 1
    if solution[0] == target:
        break
    noun += 1
    verb = 0
