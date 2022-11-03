def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    a,b = 0,0
    while i < len(list1):
        if list1[i] == 1:
            a += 1
        else:
            b += 1
        i += 1
    ans = [].append(a)
    ans.append(b)
    return ans