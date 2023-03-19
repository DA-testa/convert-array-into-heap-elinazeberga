# python3

def heaps(data, size, j, swap):
    small = j
    right = 2*j+2 ## right child n
    left = 2*j+1 ## left child n

    if left < size and data[small]:
        small = left
    if right < size and data[right]<data[small]:
        small = right
    if j != small:
        swap.append((j, small))
        data[j], data[small] = data[small], data[j]
        heaps(data, size, small, swap)


def build_heap(data):
    swaps = []
    size = len(data)
    i = size // 2-1
    for i in range(size//2, -1, -1):
        heaps(data, size, i, swaps)
        i = i+1
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


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
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
   
    
    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
