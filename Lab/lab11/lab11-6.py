def union(A,B):
    result = [int(k) for k in A]
    B = [int(k) for k in B]
    for i in B:
        if i in result:
            continue
        result.append(int(i))
    return sorted(result)

A = input('Input set A: ').split()
B = input('Input set B: ').split()

print('A union B:',union(A,B))