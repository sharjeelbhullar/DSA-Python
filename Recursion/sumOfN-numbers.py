#Parametrised Way
def fun(i, sum):
    if i < 1:
        print(sum)
        return
    fun(i-1, sum+i)

#Functional Way
def f(n):
    if n == 0:
        return 0
    return n + f(n-1)

if __name__ == '__main__':
    n = 3
    fun(n, 0)   #Parametrised Way
    f(n)    #Functional Way
