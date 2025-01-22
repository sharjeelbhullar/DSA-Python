def fun(i, n):
    if i<1:
        return
    fun(i-1, n)
    print(i)

if __name__ == "__main__":
    n = 4
    fun(n, n)