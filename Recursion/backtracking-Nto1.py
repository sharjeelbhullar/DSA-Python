def fun(i, n):
    if i>4:
        return
    fun(i+1, n)
    print(i)

if __name__ == "__main__":
    n = 4
    fun(1, n)