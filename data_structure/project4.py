sentence = "Hi Alex WelcomeAlex Bye Alex"

words = sentence.split()

count = 0

for word in words:
    if word.count("Alex"):
        count += word.count("Alex")

print(count)