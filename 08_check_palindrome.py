text = input(" Enter a number or Text : ")

# Reverse the text
reversed_text = text[::-1]

if text == reversed_text:
    print(text, "is a Palindrome.")
else:
    print(text, "is Not a Palindrone.")