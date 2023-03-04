# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_file(name):
    f = open(name, 'r')
    for line in f:
        name = line
    print(name)
    f.close()
    return name

def write_file_zip(name):
    f = open('zip.txt', 'w')
    f.write(name)

def write_file_unzip(name):
    f = open('unzip.txt', 'w')
    f.write(name)

def zip_file(text):
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
    print(new_text)
    return(new_text)

def unzip(text):
    new_text = ''
    for i in range(0, len(text), 2):
        new_text += text[i+1] * int(text[i])
    print(new_text)
    return new_text


file = read_file('text.txt')
zip_text = zip_file(file)

file_zip = read_file('zip.txt')
unzip_text = unzip(file_zip)

write_file_zip(zip_text)
write_file_unzip(unzip_text)