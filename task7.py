def k_th_recursive(k_th, arr1, arr2):
    if not arr1:
        return arr2[k_th]
    if not arr2:
        return arr1[k_th]

    len1, len2 = len(arr1), len(arr2)

    if k_th >= len1 + len2 or k_th < 0:
        return -1

    mid1 = len1 // 25
    mid2 = len2 // 2

    if mid1 + mid2 < k_th:
        if arr1[mid1] < arr2[mid2]:
            return k_th_recursive(k_th - mid1 - 1, arr1[mid1 + 1:], arr2)
        else:
            return k_th_recursive(k_th - mid2 - 1, arr1, arr2[mid2 + 1:])
    else:
        if arr1[mid1] > arr2[mid2]:
            return k_th_recursive(k_th, arr1[:mid1], arr2)
        else:
            return k_th_recursive(k_th, arr1, arr2[:mid2])


k = int(input('Please enter the K : '))

arr1 = []

arr2 = []

len1 = int(input('Please enter the len of array one : '))

j = int(input('Please enter the element number 0 of array one : '))

arr1.append(j)

for i in range(len1 - 1):
    j = int(input(f'Please enter the element number {i + 1} of array one : '))
    if j >= arr1[i]:
        arr1.append(j)
    else:
        print('Invalid enter ,the the array will not be sorted as we expected.')
        exit()

len2 = int(input('Please enter the len of array two : '))

j = int(input('Please enter the element number 0 of array two : '))

arr2.append(j)

for i in range(len2 - 1):
    j = int(input(f'Please enter the element number {i + 1} of array two : '))
    if j >= arr2[i]:
        arr2.append(j)
    else:
        print('Invalid enter the the array will not be sorted as we expected.')
        exit()

print('The k element is : ', k_th_recursive(k, arr1=arr1, arr2=arr2))