phrase = "Hello World!"
print(phrase)
print(phrase + " Hope it ends soon!")
print(phrase)


phrase = "HeLlO WoRlD!"
print(phrase.lower())
print(phrase.upper())
print(phrase)


phrase = "HeLlO WoRlD!"
print(phrase.isupper())


phrase = "HeLlO WoRlD!"
print(phrase.upper().isupper())


phrase = "HeLlO WoRlD!"
print(len(phrase))


phrase = "HeLlO WoRlD!"
#         012345678901
print(phrase[0])


phrase = "Hello world!"
print(phrase.index("e"))
print(phrase.index("world"))
print(phrase.index("z"))
print(phrase.index("E"))


phrase = "Hello world!"
print(phrase.replace("Hello", "Goodbye"))