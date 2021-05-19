
dict = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и", "Й", "й", "К", "к",
        "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р",
        "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч",
        "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Э", "э", "Ю", "ю",
        "Я", "я", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?", "!",".", ",", " "]

phraz = "йХСЛЧЪЁ ,ЁТЛЩД"

codes = [ dict.index(ch) for ch in phraz ]
for delta in range(len(dict)):
    shift = []
    decode = []
    for code in codes:
        newcode = code + delta
        if newcode >=  len(dict):
            newcode = delta - code
        shift.append(newcode)
    for sh in shift:
        decode.append(dict[sh])
    print("".join(decode))