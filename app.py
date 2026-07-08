# Reading text from a file

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("========== ORIGINAL TEXT ==========\n")
print(text)