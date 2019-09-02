fin = open('words.txt')

for word in fin:
    if len(word.strip()) > 20:
        print(word)
