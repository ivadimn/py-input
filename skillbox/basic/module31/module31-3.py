import re


text = "Even if they are djinns, I will get djinns that can outdjinn them."

pattern =r"\b[aeyuiojAEYUIIJ]\w*"
pattern1 =r"\b[^aeyuiojAEYUIIJ\s]\w+"

result = re.findall(pattern, text)
print(result)

result = re.findall(pattern1, text)
print(result)

dates = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"

pattern2 =r"\b\d{2}-\d{2}-\d{4}"
result = re.findall(pattern2, dates)
print(result)