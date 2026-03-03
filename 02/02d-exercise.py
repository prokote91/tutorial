text = "python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science, and automation. The synthax is clean and readable. This makes python perfect for beginners and experts alike. "

print(len(text))  # character
print(len(text.split()))  # word


sentence_count = 0  # sentence
for char in text:
    if char in ".!?":
        sentence_count = sentence_count+1
print(sentence_count)
