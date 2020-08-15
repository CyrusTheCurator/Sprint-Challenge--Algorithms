'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if "th" in word:
        begindex = (word.index("th")) + 2
        count = (count_th(word[begindex:len(word)])) + 1
        return count
    else:
        return 0
    return count
    



print(count_th("there are many things in the thought of this then."))