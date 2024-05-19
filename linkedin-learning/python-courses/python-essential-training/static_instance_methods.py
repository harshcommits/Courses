class WordList:
    def __init__(self):
        self.words = set()


    def addText(self, text):
        text = self.clearText(text)

    def clearText(self, text):
        # chaining functions
        text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')

if __name__ == "__main__":

    wordlist = WordList()