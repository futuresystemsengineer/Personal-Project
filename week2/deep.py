answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
answer_lower = answer.lower()

if answer_lower in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")