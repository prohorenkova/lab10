a = {}

with open("en-ru.txt", "r") as file:
    for line in file:
        en_words = line.split("-")[0].strip()
        ru_words = line.split("-")[1].strip().split(',')
        for i in ru_words:
            i = i.strip()
            if i not in a.keys():
                a[i] = en_words
            else:
                a[i] = a[i] + ", " + en_words

with open("ru-en.txt", "w") as file:
    for i in sorted(a.keys()):
        file.writelines(f"{i} - {a[i]}\n")
