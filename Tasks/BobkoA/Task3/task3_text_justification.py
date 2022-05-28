
def readFileContent():
 import pathlib

 file = open(r'..\..\AnastasiyaBobko_PY\Md-PT1-48-22\Tasks\BobkoA\Task3\text.txt', 'r')
 all_of_it = file.read()
 file.close()
 return all_of_it.split(" ")


def readMaxLen():
 while True:
     try:
         maxLen = int(input("Введите число от 35 до 50: "))
     except ValueError:
         print("Не число! Введите число. ")
         continue
     else:
         if not 35 <= maxLen <= 50:
              print("Значение должно быть в интервале от 35 до 50 включетельно. Попробуйте снова. ")
              continue
         if 35 <= maxLen <= 50:
             return maxLen
         break


def formattedText(words):
 width = 0
 current_line = 0
 word_list = []
 
 for i in range(len(words)):

        width += len(words[i])
        if i > 0:
            width += 1
       
        if width > maxLen:
            break
        word_list.append(words[i])
        current_line += len(words[i])
 else: 
        result = ' '.join(word_list)
        result += ' ' * (maxLen - len(result))
        return [result]
    
 space_count = maxLen - current_line 
 word_count = len(word_list)
 if word_count == 1: 
        result = word_list[0] + ' ' * space_count
 else:
        result = word_list[0]
        basic, extra = divmod(space_count, word_count - 1)
        for j in range(1, word_count):
            if j <= extra:
                result += ' '
            result += ' ' * basic + word_list[j]
 return [result] + formattedText(words[i:])


words = readFileContent()
maxLen = readMaxLen()

outputFile = open('outputtext.txt', 'w')
outputFile.write('\n'.join(formattedText(words)))
outputFile.close()

print("Текст отредактирован и доступен для чтения в файле outputtext.txt")