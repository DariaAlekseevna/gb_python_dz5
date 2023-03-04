# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_file(name):
    f = open(name, 'r')
    for line in f:
        name = line
    print(f'исходный файл: {name}')
    f.close()
    return name

def write_file_compress(name):
    f = open('compress.txt', 'w')
    f.write(name)

def write_file_uncompress(name):
    f = open('uncompress.txt', 'w')
    f.write(name)

def compress_file(text):
    k = 1
    new_text = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1] and i != len(text)-2:
            k += 1
        elif text[i] != text[i+1] and i != len(text)-2:
            new_text += str(k) + text[i]
            k = 1
        elif text[i] == text[i+1] and i == len(text)-2:
            new_text += str(k+1) + text[i]
            k = 1
        else:
            new_text += str(k) + text[i] + '1' + text[i+1]         
    print(f'сжатый файл: {new_text}')
    return(new_text)

def uncompress(text):
    new_text = ''
    for i in range(0, len(text), 2):
        new_text += text[i+1] * int(text[i])
    print(f'восстановленный файл: {new_text}')
    return new_text

file = read_file('text.txt')
compress_text = compress_file(file)
write_file_compress(compress_text)

file_compress = read_file('compress.txt')
uncompress_text = uncompress(file_compress)
write_file_uncompress(uncompress_text)