
dict = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и", "Й", "й", "К", "к",
        "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р",
        "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч",
        "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Э", "э", "Ю", "ю",
        "Я", "я", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?", "!",".", ",", " "]

phraz = "йХСЛЧЪЁ ,ЁТЛЩД"
phraz2 = "шИРКНЗМЧУНЩЬЗЪЫЧФ?УЧЗФНЫЕ"
l = len(dict)
codes = [dict.index(ch) for ch in phraz2]
print(codes)

for delta in range(l):
    shift = []
    decode = []
    for code in codes:
        new_code = code + delta
        if new_code >= len(dict):
            new_code = new_code - l
        #print(new_code)
        shift.append(new_code)
    for sh in shift:
        decode.append(dict[sh])
    print("".join(decode), delta, dict[delta] )