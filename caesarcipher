import string

# Let's look at the lowercase letters.
alphabet = ' ' + string.ascii_lowercase
positions = {ch:alphabet.index(ch) for ch in alphabet}

message = "hi my name is caesar"

def encode(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string    

# otra opcion de la funcion encode usando list comprehensions
def enc(msg, key):
    encoding_list = [alphabet[(positions[char] + key) % 27] for char in message]
    return "".join(encoding_list)

encoded_message = encode(message, 3)
decoded_message = encode(encoded_message, -3)
print(encoded_message)
print(decoded_message)
