def fun(i, n):
    if i>n:
        return
    print(i)
    fun(i+1, n)

if __name__ == "__main__":
    fun(1, 4)