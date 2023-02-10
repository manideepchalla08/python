import itertools

n=list(map(int,input("entre the numbers separeted by space=").strip().split()))

permutations=list(itertools.permutations(n))

print(permutations)
