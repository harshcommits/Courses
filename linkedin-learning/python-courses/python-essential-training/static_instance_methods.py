# need to read up on the @staticmethod decorator

class WordList:
    Puncs = [',', '.', '!', '\'']
    def __init__(self):
        self.words = set()


    def addText(self, text):    # example of an instance method
        text = WordList.clearText(text)
        for word in text.split():
            self.words.add(word)

    def clearText(text):    # self keyword not required since this is a static method, and therefore linked to the class itself
        # chaining functions
        # text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
        for punc in WordList.Puncs:
            text = text.replace(punc, '')
        return text.lower()

if __name__ == "__main__":

    wordlist = WordList()
    wordlist.addText("Hello, I am Harsh! Here is some text I want to test here.")

    print(wordlist.words)