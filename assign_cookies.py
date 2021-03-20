def assign_cookies(child_greediness, cookie_sizes):
    child_greediness.sort()
    cookie_sizes.sort()

    cookies_assigned = 0
    i = 0
    j = 0

    while (i < len(child_greediness)) and (j < len(cookie_sizes)):
        if(cookie_sizes[j] >= child_greediness[i]):
            cookies_assigned+=1
            i+=1
            j+=1
        else:
            j+=1
    return cookies_assigned


if __name__ == "__main__":
    test_childs = [3, 2, 1, 1, 1, 4, 5, 3, 2, 1, 3]
    test_cookies = [3, 3, 3, 3, 3, 3, 3, 5, 6, 6, 2, 3, 4, 2]
    result = assign_cookies(test_childs, test_cookies)
    print(result)
    
