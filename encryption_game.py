from essential_generators import DocumentGenerator
import random

def encryption(sentence_in, key=-random.randint(1, 5)):
    sentence_out = ''
    alpha_a = 'abcdefghijklmnopqrstuvwxyz'
    alpha_b = alpha_a[key:] + alpha_a[:key]

    for letter_in in sentence_in:
        uppercase = letter_in.isupper()
        letter_in = letter_in.lower()
        
        if letter_in in alpha_a:
            position = alpha_a.index(letter_in)
            letter_out = alpha_b[position]
            if uppercase:
                sentence_out += letter_out.upper()
            else:
                sentence_out += letter_out

        else:
            sentence_out += letter_in
    
    return -key, sentence_out


gen = DocumentGenerator()
sentance_secret = gen.sentence()
encryption_key, sentance_encrypted = encryption(sentance_secret)

print('encrypted sentance is:\n', sentance_encrypted)

guess = ''

while guess != encryption_key:
    guess = int(input())
    _, unencrypted_sentence = encryption(sentance_encrypted, guess)
    print(unencrypted_sentence)

print('correct!')
