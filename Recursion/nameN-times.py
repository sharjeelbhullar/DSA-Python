def fun(i, N):
    if i > N:
        return
        
    print("Sherry")
    fun(i + 1, N)

if __name__ == "__main__":
    fun(1, 4)