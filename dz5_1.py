# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абвТекст — зафиксированнаяабв на каком-либо материальном абв носителе человечабвескаяабв мысль; в общем абвплане связная и полабвная абвпоследовательность символов.'

def text_to_list(text):
    text_list = text.split(' ')
    return text_list

def del_abc(text_list):
    new_text_list = text_list.copy()
    for i in range(len(text_list)):
        if 'абв' in text_list[i]:
            new_text_list.remove(text_list[i])
    return new_text_list

def list_to_text(text_list):
    text = ''
    for i in range(len(text_list)):
        text += text_list[i] + ' '
    return text

print(text)
my_list = text_to_list(text)
new_text = list_to_text(del_abc(my_list))
print(new_text)