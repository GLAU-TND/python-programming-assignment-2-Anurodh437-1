def largestNumber(array):
    new_list, ans = [], " "
    l = len(str(max(array))) + 1

    for i in array:
        temp = str(i) * l
        new_list.append((temp[:l:], i))
    new_list.sort(reverse=True)
    for i in new_list:
        ans += str(i[1])

    return ans
b=input("Enter the input seperated by commas")
a = b.split(',')
print(a)
print (largestNumber(a))