if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = float('-inf')
    second_max = float('-inf')
    
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num != max_val:
            second_max = num

    print(second_max)
