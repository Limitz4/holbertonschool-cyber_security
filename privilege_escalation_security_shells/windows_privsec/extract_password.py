import re
import base64

path = r"C:\Windows\Panther\Unattend.xml"
with open(path, "r", errors="ignore") as f:
    content = f.read()

matches = re.findall(r"<Value>(.*?)</Value>", content, re.DOTALL)
for m in matches:
    m = m.strip()
    if len(m) > 5:
        print("Deger: " + m)
        try:
            d = base64.b64decode(m + "==").decode("utf-8")
            print("Decoded: " + d)
        except:
            pass
