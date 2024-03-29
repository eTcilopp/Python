"""
6.Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
# Функция принимает слово и заменяет первый символ на Upper Case этого символа
def int_func(text):
    return text.replace(text[0], text[0].upper(),1)

# Функция принимает строку из слов, разбивает строку на слова (разделение - через пробел)
# К каждому из слов применяется функция int_func. Из получившегося списка вновь собирается
# строка, которую и возвращает функция.
def sentence_split(sentence):
    sentence = [int_func(word) for word in sentence.split()]
    return ' '.join(sentence)

word = input('Введите слово из маленьких латинских букв ')
print(f'Результат обработки слова {word} - {int_func(word)}.')

sentence = input('Введите строку из слов, разделенных пробелом ')
print(f'Результат обработки строки {sentence} -\n{sentence_split(sentence)}.')

