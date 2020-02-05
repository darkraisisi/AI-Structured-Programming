textToWrite = "   wow look here is text\n              Lorem ipsum dolor sit amet,\tconsectetur adipiscing elit.\nSuspendisse eu mauris massa. Cras tristique elit sit amet nulla dignissim, id egestas ipsum elementum.\n\n\nCras tempor dictum neque sit amet convallis.\nVivamus porta erat enim, at maximus quam viverra nec.\n  \nPellentesque accumsan, ipsum et sagittis vehicula, dui magna elementum tortor, ac porta justo magna a ipsum. Nam bibendum hendrerit tempus. Maecenas hendrerit lobortis ligula vitae maximus. Sed posuere auctor justo, ultrices semper velit suscipit ac. Etiam vel mattis diam, ac vestibulum elit. Morbi non bibendum orci. Aenean bibendum purus sed massa interdum iaculis. Maecenas varius eget nisi a vestibulum. Sed ante enim, feugiat non elit quis, mattis volutpat dolor."
FOLDERNAME = "Formatieve Opdracht 1/"
FILENAME = "tesfile_opdracht8.txt"

def writeToFile(text, fileName):
    file = open(fileName,"w")
    file.write(text)
    file.close()

def compressString(_string):
    _string = _string.strip()
    _string = " ".join(_string.split())
    _string = _string.replace('\n','')
    _string = _string.replace('\t','')
    return _string

def compressFileContent(fileName):
    file = open(fileName,"r")
    content = file.read()
    newContent = compressString(content)
    writeToFile(newContent,FOLDERNAME+FILENAME)

writeToFile(textToWrite,FOLDERNAME+FILENAME)
compressFileContent(FOLDERNAME+FILENAME)