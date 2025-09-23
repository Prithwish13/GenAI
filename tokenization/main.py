import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Prithwish"
tokens = enc.encode(text)
print(tokens)

decoded = enc.decode(tokens)

print(decoded)

