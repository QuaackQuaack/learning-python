#solving runner.py with map method

if __name__ == '__main__':
    n = int(input())
    arr = list(int(i) for i in input().split())
    arr.sort(reverse = True)
    elements = arr[0]
    for result in arr:
        if result !=  elements:
            print(result)
            break

