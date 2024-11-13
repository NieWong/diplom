from rapidfuzz import process

class MisspellingCorrector:
    def __init__(self, vocab, threshold=70):
        self.vocab = [v.lower() for v in vocab]
        self.threshold = threshold

    def correct(self, tokens):
        corrected_tokens = []
        for word in tokens:
            word = word.lower()
            result = process.extractOne(word, self.vocab)
            if result is not None:
                match, score = result[0], result[1]
                if score >= self.threshold:
                    corrected_tokens.append(match)
                else:
                    corrected_tokens.append(word)
            else:
                corrected_tokens.append(word)
        return corrected_tokens
