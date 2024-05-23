def translate(phrase):
    translation = ""
    for i in phrase: # to check all letters
        if i.lower() in "aeiou":  # if i  in "AEIOUaeiou"
            if i.isupper():
                translation = translation +"G"
            else:
                translation = translation + "g"  # replace it with "g"
        else:
            translation = translation + i
    return translation

print(translate(input("Enter a phrase")))