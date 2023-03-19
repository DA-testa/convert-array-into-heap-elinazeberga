# python3

def heaps(data, size, i, swap):
    small = i
    right = 2*i+2 ## right child n
    left = 2*i+1 ## left child n

    if left < size and data[small]:
        small = left
    if right < size and data[right]<data[small]:
        small = right
    if j != small:
        swap.append((i, small))
        data[i], data[small] = data[small], data[i]
        heaps(data, size, small, swap)


def build_heap(data):
    swaps = []
    size = len(data)
    j = size // 2-1
    for j in range(size//2, -1, -1):
        heaps(data, size, j, swaps)
        j = j+1
    return swaps


def main():
    choice = input()
    if "F" in choice:
        fileName = input()
        if "a" in fileName:
            return ("Incorrect file name")
        with open("./tests/" + fileName, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    elif "I" in choice:
        n = int(input())
        data = list(map(int, input().split()))
   
    assert len(data) == n
    
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
