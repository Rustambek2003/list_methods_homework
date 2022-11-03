def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    ans = []
    while i < len(fruits):
        if fruits[i] == 'apple':
            ans.append(i)
        i += 1
    ans.insert(0,len(ans))
    return ans
print(main(["apple", "banana", "apple", "pear", "apple"]))