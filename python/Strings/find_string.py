def find_substring(string, sub_string):
    count=0
    for i in range(0,len(string)-2):
        if string[i:(i+len(sub_string))]==sub_string:
            count =count+1 
    return count
