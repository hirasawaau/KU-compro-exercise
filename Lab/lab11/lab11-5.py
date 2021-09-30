def minusSet(A,B):
    result = [int(i) for i in A if not i in B]
    if len(result) > 0:
        return result
    else:
        return 'empty set'
    
A = input('Input set A: ').split()
B = input('Input set B: ').split()

print('A minus B:',minusSet(A,B))