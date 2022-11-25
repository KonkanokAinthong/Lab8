OKGREEN = '\033[92m'
OKCYAN = '\033[96m'
WARNING = '\033[93m'
ENDC = '\033[0m'
data = [29, 10, 14, 37, 14, 20, 7, 16, 12]


def PrintColorData(data, i, j, mid):
    for index, value in enumerate(data):
        if index == i:
            print(OKGREEN + str(value) + ENDC, end=" ")
        elif index == mid:
            print(WARNING + str(value) + ENDC, end=" ")
        elif index == j:
            print(OKCYAN + str(value) + ENDC, end=" ")
        else:
            print(value, end=" ")
    print()


def HoareQuicksort(data, start, end):
    if start < end:
        pivot = HoarePartition(data, start, end)
        HoareQuicksort(data, start, pivot - 1)
        HoareQuicksort(data, pivot + 1, end)


def HoarePartition(data, start, end):
    if start-end == 1:
        return
    i = start-1
    j = end+1
    mid = (start+end+1) // 2
    pivot = data[mid]
    PrintColorData(data, start, end, mid)
    while True:
        i += 1
        while data[i] < pivot:
            i += 1
        j -= 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            print()
            return j
        PrintColorData(data, i, j, mid)
        data[i], data[j] = data[j], data[i]
        PrintColorData(data, i, j, mid)


print("Original array:", data)
HoareQuicksort(data, 0, len(data) - 1)
print("Sorted Array", data)