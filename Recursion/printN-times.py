cnt = 0

def print_count():
    global cnt
    
    if cnt == 3:
        return
    
    print(cnt)
    
    cnt += 1
    print_count()

if __name__ == "__main__":
    print_count()

