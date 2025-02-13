from string import ascii_letters
def chartopos(letter): # converts a letter to its alphabetical position
    return ord(letter) - 96

def postochar(pos): # converts alphabetical position to letter
    return chr(pos + 96)

def strcheck(text):
    try:
        if len(text) == 0:  # missing text
           raise ValueError
        elif type(text) is not str:  # input is not string
            raise TypeError
        else:
            return text
    except ValueError:
        print("no text put in")
    except TypeError:
        print("this is not text")

class Data:
    def __init__(self, text, key, ed, file):
        self.text = strcheck(text)
        self.key = strcheck(key)
        self.ed = ed
        self.file = file

    def vignere(self):
        code = ""
        try: # checks if encode-decode has proper value
            if self.ed == 1 or self.ed == -1:
                pass
            elif self.ed == "crypt": # converts text ed into numerical
                self.ed = int(1)
            elif self.ed == "decrypt":
                self.ed = int(-1)
            else:
                raise ValueError
        except ValueError:
            print("Wrong encode-decode value")

        if len(self.key) < len(self.text):  # modifies the key, if it is shorter than the text
            self.key *= (len(self.text) // len(self.key) + 1)

        for pos, let in enumerate(self.text):  # goes through the letters of the text
            if let.isupper():  # marks uppercase letters for later
                up = True
                let = let.lower()
            else:
                up = False
            sol = chartopos(let)
            if let in ascii_letters:  # encrypts current letter according to the key
                sol += chartopos(self.key[pos]) * self.ed

            if sol < 0 and sol != chartopos(let):  # wrap-around if the index is smaller than the alphabet
                sol += 26
            elif sol > 26 and sol != chartopos(let):  # wrap-around if the index is greater than the alphabet
                sol -= 26

            if up:
                code += (postochar(sol).upper())  # adds uppercase letter to list, when marked
            else:
                code += (postochar(sol))  # adds lowercase letter to list
        return code

    def fileout(self):
        with open("%s" % self.file, 'a', ) as f:
            if self.ed == "crypt" or self.ed == 1:
                f.write("".join(["\nplaintext: ", self.text, " key: ", self.key]))
                f.write("".join(["\nencrypted: ", self.vignere()]))
            elif self.ed == "decrypt" or self.ed == -1:
                f.write("".join(["\nencrypted text: ", self.text, " key: ", self.key]))
                f.write("".join(["\ndecrypted: ", self.vignere()]))
            elif self.ed != "decrypt" and self.ed != "crypt" and self.ed != 1 and self.ed != -1:
                f.write("\nmissing signifier whether to encode or decode (crypt/decrypt, 1/-1)")
            else:
                f.write("\nbad input")
            f.close()

class filein:
    def __init__(self, file):
        self.file = file

    def fileloop(self):
        with open("%s" % self.file, 'w') as file: # cleans out output file before writing into it
            for line in file:
                lst = line.rstrip().split('; ')  # Read next line and split into components
                if len(lst) < 3:
                    continue
                Data(lst[0], lst[1], lst[2], "output.txt").fileout()  # inputs text, key, and ed from list
            file.close()

# ed is encode-decode switch - 1 encodes, -1 decodes
F1 = filein('cipher.txt')
F1.fileloop()
