import re
def v(pn):
    if pn.startswith("+"):
        match = re.match(r"^\+(\d{2}) (\d{10})$",pn)
        if match:
            return "Correct"
    if len(pn)==10 and pn.isdigit():
        return "Correcrt"
    return "Incorrect"
pn = input().strip()
print(v(pn))
