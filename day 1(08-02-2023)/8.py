def is_valid_number(s):
    try:
        float(s)
        return True
    except valueerror:
        return False
s=(input("entre a string:"))
if (s.isdigit()):
    if is_valid_number(s):
        print(s,"true")
    else:
        print(s,"false")
else:
    print("false")
