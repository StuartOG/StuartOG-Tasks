
def caeser_cypher(sentence, shift):
    cypher = ""


    for char in sentence:
        if char.isalpha():
        
            char_shift = chr((ord(char) - ord('a') + shift % 26) + ord('a'))
            cypher += char_shift
        
        else:
        
            cypher += char

    return cypher

sentence = input("Enter a sentence: ")



shift = int(input("Give a number to shift by: "))

cypher = caeser_cypher(sentence, shift)
print(cypher)






