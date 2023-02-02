def fibMemo(n, memo) :
    if n in memo :
        return memo[n]

    if n <= 1 :
        return 1
    
    res = fibMemo(n-1, memo) + fibMemo(n-2, memo)

    memo[n] = res

    return res

n = int(input("enter n : "))
memo = {}
print(fibMemo(n, memo))