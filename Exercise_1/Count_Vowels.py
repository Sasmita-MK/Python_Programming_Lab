sent = input("Enter a string : ")
sent = sent.lower()
cnt = 0
for s in sent:
    if s== 'a' or s== 'e' or s== 'i' or s== 'o' or s== 'u':
        cnt += 1
print("There are " + str(cnt) + " vowels in the string " + sent)