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

    alphabet_reverse = None

    def __init__(self):
        self.first_key = None
        self.second_key = None
        self.message = None
        self.seed = None
        self.role = None

    def set_inputs(self, first_key, second_key, message, role=0):
        self.first_key = first_key
        self.second_key = second_key
        self.message = message
        self.role = role
        if self.role:
            self.message = list(self.message.replace('$', ' '))
        inputs_data_error = self._test_inputs()
        if inputs_data_error:
            return inputs_data_error
        self._get_seed()
        self._initialize_alphabets()

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

    def _get_seed(self):
        if not self.first_key.isnumeric():
            transformed_first_key = ''
            for symbol in self.first_key:
                transformed_first_key += str(self.alphabet[symbol])
            self.first_key = transformed_first_key

        if not self.second_key.isnumeric():
            transformed_second_key = ''
            for symbol in self.second_key:
                transformed_second_key += str(self.alphabet[symbol])
            self.second_key = transformed_second_key

        self.seed = ((len(self.first_key) + len(self.second_key)) * len(self.message) +
                     (int(self.first_key) + int(self.second_key)) * sum(map(int, self.first_key + self.second_key)))

    def _initialize_alphabets(self):
        random.seed(self.seed)
        keys = list(self.alphabet.keys())
        values = list(self.alphabet.values())
        random.shuffle(keys)
        random.shuffle(values)
        self.alphabet = dict(zip(keys, values))

        self.alphabet_reverse = {v: k for k, v in self.alphabet.items()}

    def encrypt(self):
        encrypt_message = []
        if self.role:
            self.message = self._shuffle(input_list=self.message)
        for symbol in self.message:
            encrypt_message.append(self.alphabet[symbol])
        for j in range(0, len(encrypt_message)):
            random.seed(self.seed * j)
            if self.role:
                shift = encrypt_message[j] - random.randint(1, len(self.alphabet))
                if shift < 1:
                    shift += len(self.alphabet)
            else:
                shift = encrypt_message[j] + random.randint(1, len(self.alphabet))
                if shift > len(self.alphabet):
                    shift -= len(self.alphabet)
            encrypt_message[j] = shift
        for i in range(0, len(encrypt_message)):
            encrypt_message[i] = self.alphabet_reverse[encrypt_message[i]]
        if not self.role:
            encrypt_message = self._shuffle(input_list=encrypt_message)
            encrypt_message = ''.join(encrypt_message).replace(' ', '$')
        else:
             encrypt_message = ''.join(encrypt_message).replace('$', ' ')

        return encrypt_message

    def _shuffle(self, input_list):
        for shuffle in range(0, len(input_list)):
            if self.role:
                shuffle = (len(input_list)-1) - shuffle
            random.seed(self.seed + shuffle)
            first_element = random.randint(0, len(input_list) - 1)
            random.seed(self.seed - shuffle)
            second_element = random.randint(0, len(input_list) - 1)

            input_list[first_element], input_list[second_element] = (
                input_list[second_element], input_list[first_element])

        return input_list


obj = Encoder()
obj.set_inputs('First', '125678', 'Oр,зШ+-фO7Ст', 1)
res = obj.encrypt()
print(res)

