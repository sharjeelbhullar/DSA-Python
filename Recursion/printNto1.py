def fun(i, n):
    if i<1:
        return
    print(i)
    fun(i-1, n)

if __name__ == "__main__":
    n = 4
    fun(n, n)