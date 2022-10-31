#Q41
def count_hashtag(string, target):
    total=0
    index=0
    while index<len(string):
        if string[index:index+len(target)]==target:
            total+=1
            index+= len(target)
        else:
            index+=1
    return total

count_hashtag("#compsci #college #class", "#")

#Q42
def hash_spam(string, target):
    total=0
    index=0
    while index<len(string):
        if string[index:index+len(target)]==target:
            total+=4
            index+= len(target)
            print("this tweet will be considered as a spam!")
        else:
            index+=4
            return None
    return total

count_hashtag("#compsci #college #class", "#")
