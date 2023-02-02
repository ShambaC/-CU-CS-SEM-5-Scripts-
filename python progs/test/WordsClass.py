class PyWords :
    def __init__(self, words) :
        self.process_words = words

    def words_with_length(self, size = 1) :
        res = []
        for i in range(len(self.process_words)) :
            if len(self.process_words[i]) == size :
                res.append(self.process_words[i])
        return res

    def starts_with(self, chara = 's') :
        res = []
        for words in self.process_words :
            if words[:1:] == chara :
                res.append(words)
        return res

    def palindromes(self) :
        res = []
        ignore = self.words_with_length(1)
        for word in self.process_words :
            if word not in ignore :
                if word == word[::-1] :
                    res.append(word)
        return res

l1 = ['hello', 'sun', 'swallow', 'a', 'b', 'suck', 'c', 'malayalam', 'abba', 'lol']
W = PyWords(l1)
print(W.words_with_length())
print(W.starts_with())
print(W.palindromes())