#L91
def breakify (string):
    new="<br>".join(string)
    print(new)

lines=["Haiku frogs in snow", "A limerick came from Nantucket", "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

breakify(lines)

#L92
def remove_substring(string,sub):
    output= []
    index=0
    while index < len(string):
        if string[index:index+len(sub)]== sub :
            index += len(sub)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))


remove_substring("Hello, test this is a test to see if the string removes test", "test")

#L93
def replace_substring(string,remove,add):
    output= []
    index=0
    while index < len(string):
        if string[index:index+len(remove)]== remove :
            index += len(remove)
            output.append(add)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

replace_substring("Hello, I am error how to code!", "error", "learning")
