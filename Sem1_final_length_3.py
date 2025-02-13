def strcheck(text):
    try:
        if len(text) == 0:  # text missing
           raise ValueError
        elif type(text) is not str:  # input is not string
            raise TypeError
        else:
            return text
    except ValueError:
        print("no text has been put in")
    except TypeError:
        print("this is not text")

class wordlen:
    def __init__(self, text):
        self.text = strcheck(text)

    def minl(self):
        words = ''.join(char for char in self.text if char.isalnum() or char.isspace()) #cleans up string
        words = words.split() # changes the string into an array of words
        minl = len(words[0])  # sets initial value
        short = []
        for i in words:  # goes through words
            if len(i) < minl: #if the word is the new shortest
                minl = len(i) #sets new length to beat
                short = [i] #overwrites current list
            elif len(i) == minl: # if of equal length, adds to the list
                short.append(i)
        return ", ".join(short)

    def maxl(self):
        words = ''.join(char for char in self.text if char.isalnum() or char.isspace())  # cleans up string
        words = words.split()  # changes the string into an array of words
        maxl = len(words[0])  # sets initial value
        long = []
        for i in words: # goes through words
            if len(i) > maxl: #if the word is the new longest
                maxl = len(i) #sets new length to beat
                long = [i] #overwrites current list
            elif len(i) == maxl: # if of equal length, adds to the list
                long.append(i)
        return ", ".join(long)

class filestats:
    def __init__(self, file):
        self.file = file
    def textls(self):
        with open("%s" % self.file, 'r+') as file:  # saves in the lists of longest and shortest words
            cls = wordlen("".join(file.readlines()).rstrip())
            file.write("".join(["\n shortest: ", cls.minl(), "; longest: ", cls.maxl()]))
            file.close()


F1 = filestats("text.txt")
F1.textls()
