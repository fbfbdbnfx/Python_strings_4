s=str.lower(input()).split(' ')

count_words={i:s.count(i) for i in s}

print(count_words)

sorted_count=sorted(count_words.items(), key=lambda x: x[1])[::-1]

print(sorted_count[0:5])
