import random


class Encoder:
    alphabet = {'й': 1, 'ц': 2, 'у': 3, 'к': 4, 'е': 5, 'н': 6, 'г': 7, 'ш': 8, 'щ': 9, 'з': 10, 'х': 11, 'ъ': 12,
                'ф': 13, 'ы': 14, 'в': 15, 'а': 16, 'п': 17, 'р': 18, 'о': 19, 'л': 20, 'д': 21, 'ж': 22, 'э': 23,
                'я': 24, 'ч': 25, 'с': 26, 'м': 27, 'и': 28, 'т': 29, 'ь': 30, 'б': 31, 'ю': 32, 'ё': 33, '.': 34,
                ',': 35, ' ': 36, '!': 37, '?': 38, '-': 39, 'Ю': 40, 'Б': 41, 'Ь': 42, 'Т': 43, 'И': 44, 'М': 45,
                'С': 46, 'Ч': 47, 'Я': 48, 'Ф': 49, 'Ы': 50, 'В': 51, 'А': 52, 'П': 53, 'Р': 54, 'О': 55, 'Л': 56,
                'Д': 57, 'Ж': 58, 'Э': 59, 'Ъ': 60, 'Х': 61, 'З': 62, 'Щ': 63, 'Ш': 64, 'Г': 65, 'Н': 66, 'Е': 67,
                'К': 68, 'У': 69, 'Ц': 70, 'Й': 71, 'Ё': 72, '1': 73, '3': 74, '5': 75, '7': 76, '9': 77, '0': 78,
                '8': 79, '6': 80, '4': 81, '2': 82, 'q': 83, 'w': 84, 'e': 85, 'r': 86, 't': 87, 'y': 88, 'u': 89,
                'i': 90, 'o': 91, 'p': 92, 'a': 93, 's': 94, 'd': 95, 'f': 96, 'g': 97, 'h': 98, 'j': 99, 'k': 100,
                'l': 101, 'z': 102, 'x': 103, 'c': 104, 'v': 105, 'b': 106, 'n': 107, 'm': 108, 'Z': 109, 'X': 110,
                'C': 111, 'V': 112, 'B': 113, 'N': 114, 'M': 115, 'A': 116, 'S': 117, 'D': 118, 'F': 119, 'G': 120,
                'H': 121, 'J': 122, 'K': 123, 'L': 124, 'P': 125, 'O': 126, 'I': 127, 'U': 128, 'Y': 129, 'T': 130,
                'R': 131, 'E': 132, 'W': 133, 'Q': 134, '(': 135, ')': 136, '=': 137, '_': 138, '#': 139, '/': 140,
                '&': 141, '"': 142, '+': 143, ':': 144, '%': 145}
    alphabet2 = {1: 'й', 2: 'ц', 3: 'у', 4: 'к', 5: 'е', 6: 'н', 7: 'г', 8: 'ш', 9: 'щ', 10: 'з', 11: 'х', 12: 'ъ',
                 13: 'ф', 14: 'ы', 15: 'в', 16: 'а', 17: 'п', 18: 'р', 19: 'о', 20: 'л', 21: 'д', 22: 'ж', 23: 'э',
                 24: 'я', 25: 'ч', 26: 'с', 27: 'м', 28: 'и', 29: 'т', 30: 'ь', 31: 'б', 32: 'ю', 33: 'ё', 34: '.',
                 35: ',', 36: '$', 37: '!', 38: '?', 39: '-', 40: 'Ю', 41: 'Б', 42: 'Ь', 43: 'Т', 44: 'И', 45: 'М',
                 46: 'С', 47: 'Ч', 48: 'Я', 49: 'Ф', 50: 'Ы', 51: 'В', 52: 'А', 53: 'П', 54: 'Р', 55: 'О', 56: 'Л',
                 57: 'Д', 58: 'Ж', 59: 'Э', 60: 'Ъ', 61: 'Х', 62: 'З', 63: 'Щ', 64: 'Ш', 65: 'Г', 66: 'Н', 67: 'Е',
                 68: 'К', 69: 'У', 70: 'Ц', 71: 'Й', 72: 'Ё', 73: '1', 74: '3', 75: '5', 76: '7', 77: '9', 78: '0',
                 79: '8', 80: '6', 81: '4', 82: '2', 83: 'q', 84: 'w', 85: 'e', 86: 'r', 87: 't', 88: 'y', 89: 'u',
                 90: 'i', 91: 'o', 92: 'p', 93: 'a', 94: 's', 95: 'd', 96: 'f', 97: 'g', 98: 'h', 99: 'j', 100: 'k',
                 101: 'l', 102: 'z', 103: 'x', 104: 'c', 105: 'v', 106: 'b', 107: 'n', 108: 'm', 109: 'Z', 110: 'X',
                 111: 'C', 112: 'V', 113: 'B', 114: 'N', 115: 'M', 116: 'A', 117: 'S', 118: 'D', 119: 'F', 120: 'G',
                 121: 'H', 122: 'J', 123: 'K', 124: 'L', 125: 'P', 126: 'O', 127: 'I', 128: 'U', 129: 'Y', 130: 'T',
                 131: 'R', 132: 'E', 133: 'W', 134: 'Q', 135: '(', 136: ')', 137: '=', 138: '_', 139: '#', 140: '/',
                 141: '&', 142: '"', 143: '+', 144: ':', 145: '%'}
    alphabet3 = {1: 136, 2: 15, 3: 74, 4: 137, 5: 78, 6: 67, 7: 27, 8: 138, 9: 60, 10: 121, 11: 37, 12: 24, 13: 87,
                 14: 85, 15: 34, 16: 115, 17: 5, 18: 92, 19: 119, 20: 130, 21: 127, 22: 44, 23: 38, 24: 76, 25: 89,
                 26: 10, 27: 109, 28: 82, 29: 52, 30: 14, 31: 69, 32: 26, 33: 11, 34: 30, 35: 48, 36: 131, 37: 17,
                 38: 65, 39: 142, 40: 7, 41: 16, 42: 55, 43: 110, 44: 132, 45: 144, 46: 31, 47: 54, 48: 21, 49: 20,
                 50: 90, 51: 64, 52: 86, 53: 125, 54: 140, 55: 18, 56: 58, 57: 45, 58: 96, 59: 8, 60: 81, 61: 42,
                 62: 106, 63: 57, 64: 129, 65: 23, 66: 35, 67: 99, 68: 88, 69: 145, 70: 143, 71: 77, 72: 46, 73: 133,
                 74: 50, 75: 71, 76: 6, 77: 91, 78: 126, 79: 117, 80: 4, 81: 108, 82: 116, 83: 13, 84: 141, 85: 47,
                 86: 49, 87: 111, 88: 22, 89: 59, 90: 84, 91: 41, 92: 33, 93: 79, 94: 53, 95: 25, 96: 100, 97: 68,
                 98: 2, 99: 120, 100: 70, 101: 97, 102: 101, 103: 39, 104: 63, 105: 32, 106: 134, 107: 61, 108: 135,
                 109: 123, 110: 3, 111: 118, 112: 43, 113: 83, 114: 105, 115: 56, 116: 29, 117: 80, 118: 62, 119: 98,
                 120: 95, 121: 128, 122: 1, 123: 122, 124: 36, 125: 9, 126: 139, 127: 113, 128: 19, 129: 72, 130: 66,
                 131: 93, 132: 75, 133: 51, 134: 104, 135: 114, 136: 107, 137: 94, 138: 102, 139: 28, 140: 112,
                 141: 124, 142: 103, 143: 12, 144: 40, 145: 73}

    def __init__(self):
        self.first_key = None
        self.second_key = None
        self.message = None

    def set_inputs(self, first_key, second_key, message):
        self.first_key = first_key
        self.second_key = second_key
        self.message = message
        inputs_data_error = self._test_inputs()
        if inputs_data_error:
            return inputs_data_error

    def _test_inputs(self):
        if self.first_key == '' or self.second_key == '':
            return 'Ключи не могут быть пустыми'
        for key in [self.first_key, self.second_key]:
            if key.isnumeric():
                continue
            error_symbols = []
            for symbol in key:
                if symbol not in self.alphabet:
                    error_symbols.append(symbol)
            if error_symbols:
                return 'В ключах недопустимые символы: ' + ' '.join(error_symbols)
        error_letters = []
        for letter in self.message:
            if letter not in self.alphabet:
                error_letters.append(letter)
        if error_letters:
            return 'Недопустимые символы в тексте: ' + ' '.join(error_letters)

        return

    def _shuffle_hash_tables(self):
        pass
        random.seed(123)
        keys = list(self.alphabet.keys())
        values = list(self.alphabet.values())
        random.shuffle(keys)
        random.shuffle(values)
        self.alphabet = dict(zip(keys, values))

        keys = list(self.alphabet2.keys())
        values = list(self.alphabet2.values())
        random.shuffle(keys)
        random.shuffle(values)
        self.alphabet2 = dict(zip(keys, values))

        keys = list(self.alphabet3.keys())
        values = list(self.alphabet3.values())
        random.shuffle(keys)
        random.shuffle(values)
        self.alphabet3 = dict(zip(keys, values))

    def encrypt(self):
        self._shuffle_hash_tables()
        pass