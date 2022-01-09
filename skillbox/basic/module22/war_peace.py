import zipfile
import string


def frequency(text: str) -> dict:
    len_text = len(text)
    symbols = set(text)
    freq = {ch: text.count(ch) / len_text for ch in sorted(symbols)}
    return {key : freq[key] for key in sorted(freq, key=freq.get)}

exclude = string.punctuation + " 0123456789" + \
          "\u3002\u201e\u201c\u201f\u201d\u301e\u301f\u00ab\u00bb\u00b7\u00a8" + \
          "\u2116\u00a0\u00b0\u00ac\u0227\u2007\u2026\u2012\u2013\u2014\n\r\t"
table = "".maketrans("", "", exclude)
zip_file = zipfile.ZipFile("voyna-i-mir.zip")
print(zip_file.namelist())
text = ""
for fileName in zip_file.namelist():
    bytes = zip_file.read(fileName)
    content = bytes.decode("UTF-8")
    content = content.translate(table)
    text = text.join(content)
zip_file.close()

freq_table = frequency(text)
freq_file = open("wp_analysis.txt", "w")
print("\nСдержимое файла wp_analysis.txt: \n")
for k, v in freq_table.items():
    if k.isalpha():
        line = "{0} {1}\n".format(k, v)
    else:
        line = "{0} {1}\n".format(ord(k), v)
    print(line, end = "")
    freq_file.write(line)
print()
freq_file.close()