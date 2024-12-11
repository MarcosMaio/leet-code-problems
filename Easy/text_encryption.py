# Faça uma função que criptografe um texto recebendo um texto e retornando uma criptografia que transforma as letras em suas respectivas posições no alfabeto. Por exemplo, a letra 'a' é a letra 0, a letra 'b' é a letra 1, a letra 'c' é a letra 2, e assim por diante. A função deve retornar uma string com o texto criptografado.

import string

alphabet = list(string.ascii_uppercase)
text = "Mamaco"

def encrypt_text(text):
    encrypted = []
    for char in text:
      char = char.upper() 
      for j, alpha in enumerate(alphabet):
          if char == alpha:
            encrypted.append({char: j + 1})
            
    # return encrypted
    print(encrypted)
    
# def encrypt_text(text):
#     encrypted = []
#     for char in text:
#         char = char.upper()
#         if char in alphabet:
#             index = alphabet.index(char)
#             encrypted.append(str(index))
#         else:
#             encrypted.append(char)
#     encrypted_text = ' '.join(encrypted)
#     print(encrypted_text)


encrypt_text(text)