# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra. Exemplo:
# a) Entrada: palavras = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# b) Saída esperada: {'apple': 2, 'banana': 3, 'orange': 1}

from collections import Counter

word_list = list()

while True:
    word = input('Digite uma palavra qualquer:\n')
    if word.lower() == 'sair': 
        break
    else:
        word_list.append(word.lower())  

def count_words(word_list): 
    word_count = dict(Counter(word_list))
    return word_count

print(count_words(word_list))  
    
   
