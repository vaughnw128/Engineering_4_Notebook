print("String Splitter")
sent = str(input("Input your sentence: "))
splitsent = sent.split()
for i in range (0, len(splitsent)):
    templetter = list(splitsent[i])
    for x in range (0, len(templetter)):
        print(templetter[x])
    print('-')
           
