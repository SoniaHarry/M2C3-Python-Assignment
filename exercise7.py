sentence="The quick brown fox jumps over the lazy dog"
first_word= sentence[:sentence.index(' ')].upper()
new_sentence= first_word + sentence[3:]
print(new_sentence)
