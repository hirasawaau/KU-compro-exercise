

def multiply(A):
    result = 1.0
    for i in A:
        result = result*i
    return result


matrix = []
for i in range(3):
    row = [float(i) for i in input(f'Row {i+1} : ').split()]
    row.extend(row[0:3])
    matrix.append(row)

result = 0
result += multiply([matrix[i][i] for i in range(3)])
# print(result)
result += multiply([matrix[i][i+1] for i in range(3)])
# print(result)
result += multiply([matrix[i][i+2] for i in range(3)])
# print(result)

d = 0
d += multiply([matrix[i][2-i] for i in range(2,-1,-1)])
# print(d)
d += multiply([matrix[i][3-i] for i in range(2,-1,-1)])
# print(d)
d += multiply([matrix[i][4-i] for i in range(2,-1,-1)])

print(int(result-d))



