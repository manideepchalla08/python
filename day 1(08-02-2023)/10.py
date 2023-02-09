def modify_string(S):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency = [0 for i in range(26)]
    for char in S:
        frequency[ord(char) - ord('a')] += 1

    modified_string = ""
    for char in S:
        modified_string += alphabet[(ord(char) - ord('a') + frequency[ord(char) - ord('a')]) % 26]

    return modified_string
S=input("entre an string:=")
result=modify_string(S)
print(result)
