# put your python code here
words = input().lower().split(' ')
words_count = {}

for word in words:
    words_count[word] = words_count.get(word, 0) + 1

for word, count in words_count.items():
    print(f"{word} {count}")
