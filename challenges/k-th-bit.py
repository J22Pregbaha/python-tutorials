def solution(n, k):
    print(bin(n).replace("0b", ""))
    print(n, pow(2,k-1))
    return n - pow(2,k-1) if n & pow(2,k-1) else n

print(solution(37, 2))