class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence:
    def __init__(self, content):
        self.content = content
        self.show(content)
        self.show_parts(content)

    def show(self, content):
        result_show = []
        for x in content:
            result_show.append(ID[x].text)
        print(' '.join(result_show))

    def show_parts(self, content):
        result_show_parts = []
        for x in content:
            if ID[x].part not in result_show_parts:
                result_show_parts.append(ID[x].part)
        print(' '.join(result_show_parts))


words = [
        ["СЃРѕР±Р°РєР°", "СЃСѓС‰"],
        ["РµР»Р°", "РіР»Р°РіРѕР»"],
        ["СЃРїР°Р»Р°", "РіР»Р°РіРѕР»"],
        ["Р°", "СЃРѕСЋР·"],
        ["РєРѕР»Р±Р°СЃСѓ", "СЃСѓС‰"],
        ["РІРµС‡РµСЂРѕРј", "РЅР°СЂРµС‡РёРµ"]]

# РћР±СЉСЏРІР»СЏРµРј СЃРїРёСЃРѕРє РїРѕ ID
ID = []

# Р¤РѕСЂРјРёСЂСѓРµРј СЃРїРёСЃРѕРє ID РїРѕРґ РґР»РёРЅСѓ РјР°СЃСЃРёРІР°
for x in range(0, len(words)):
    z = 'word' + str(x)
    ID.append(z)

# Р—Р°РїРёСЃС‹РІР°РµС‚ Р·РЅР°С‡РµРЅРёСЏ РёР· РјР°СЃСЃРёРІР° РІ СЌРєР·РµРјРїР»СЏСЂ РєР»Р°СЃСЃР° Word
for i in range(0, len(ID)):
    y = words[i]
    ID[i] = Word(y[0], y[1])

# РџСЂРѕРІРµСЂРєР° СЂРµР·СѓР»СЊС‚Р°С‚Р°
test = Sentence([0, 2, 3, 5, 1, 4])

