def count_occurrences(string, onecharacter):
    count = 0 
    for i in range(len(string)):
        if string[i] == onecharacter:
            count= count + 1
        elif i == (len(string) - 1):
            print(count)
            return count
count_occurrences("Hello world", "o")