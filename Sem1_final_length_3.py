def strcheck(text):
    try:
        if len(text) == 0:  # text missing
           raise ValueError
        elif type(text) is not str:  # input is not string
            raise TypeError
        else:
            return text
    except ValueError:
        print("žádný text nezadán")
    except TypeError:
        print("toto není text")
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
class filewc:
    def __init__(self, file):
        self.file = file
    def filewc(self):
        with open("%s" % self.file, 'rt+') as file:  # saves in the lists of longest and shortest words
            cls = wordlen("".join(file.readlines()).rstrip())
            file.write("".join(["\n nejkratší: ", cls.minl(), "; nejdelší: ", cls.maxl()]))
            file.close()


F1 = filewc("text.txt")
F1.filewc()
