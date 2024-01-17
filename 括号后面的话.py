def text_input():
    text = input("内容：")
    a = None
    b = None
    c = None

    if "（" in text or "(" in text:
        start = text.find("（") if "（" in text else text.find("(")
        b = text[start+1:]
        c = text[:start]

    else:
        c = text

    if b and ("）" in b or ")" in b):
        end = b.find("）") if "）" in b else b.find(")")
        b = b[:end]

    if b is None or b == "" or b == "不是" or b == "bushi" or b == "doge":
        a = "不是"

    else:
        a = b
        
    print(c,"（",a,"）")
text_input()