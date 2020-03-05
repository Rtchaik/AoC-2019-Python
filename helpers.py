def fileToList(fileName='input.txt'):
  with open(fileName) as file:
    return file.readlines()
