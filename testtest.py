from translate import Translator

file = open("out.txt", "w")
translator= Translator(to_lang="spanish")
translation = translator.translate("My friend is running in the park!")
file.write(translation)