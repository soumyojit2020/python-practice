def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

if __name__ == '__main__':
    ans = linear_search([5, 2, 4, 6, 1, 3], 3)
    if ans == -1:
        print("null")
    else:
        print(ans)
        