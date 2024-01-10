import random


class Encoder:

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
        inputs_data_error = self._test_inputs()
        if inputs_data_error:
            return inputs_data_error
        self._get_seed()

    def _test_inputs(self):
        if self.first_key == '' or self.second_key == '':
            return 'Ключи не могут быть пустыми'
        for key in [self.first_key, self.second_key]:
            if key.isnumeric():
                continue
            error_symbols = []
            for symbol in key:
                try:
                    symbol.encode('utf-8')
                except UnicodeEncodeError:
                    error_symbols.append(symbol)
            if error_symbols:
                return 'В ключах недопустимые символы: ' + ' '.join(error_symbols)

        error_letters = []
        for letter in self.message:
            try:
                letter.encode('utf-8')
            except UnicodeEncodeError:
                error_letters.append(letter)
        if error_letters:
            return 'Недопустимые символы в тексте: ' + ' '.join(error_letters)

        return

    def _get_seed(self):
        if not self.first_key.isnumeric():
            transformed_first_key = ''
            for i in [byte for byte in self.first_key.encode('utf-8')]:
                transformed_first_key += str(i)
            self.first_key = transformed_first_key

        if not self.second_key.isnumeric():
            transformed_second_key = ''
            for i in [byte for byte in self.second_key.encode('utf-8')]:
                transformed_second_key += str(i)
            self.second_key = transformed_second_key

        self.seed = ((len(self.first_key) + len(self.second_key)) * len(self.message) +
                     (int(self.first_key) + int(self.second_key)) * sum(map(int, self.first_key + self.second_key)))

    def encrypt(self):
        encrypt_message = []
        if self.role:
            self.message = self._shuffle(input_list=self.message)

        for symbol in self.message:
            symbol = [byte for byte in symbol.encode('utf-8')]

            if len(symbol) == 1:
                random.seed(self.seed)

                symbol[0] += random.randint(0, 127)
                if symbol[0] > 127:
                    symbol [0] -= 127

            elif len(symbol) == 2:
                random.seed(self.seed)

                symbol[0] += random.randint(0, 31) # 223 - 192
                if symbol[0] > 223:
                    symbol[0] = (symbol[0] - 223) + 192
                elif symbol[0] < 192:
                    symbol[0] = 223 - (192 - symbol[0])

                random.seed(self.seed)
                symbol[1] += random.randint(0, 63) # 191 - 128
                if symbol[1] > 191:
                    symbol[1] = (symbol[1] - 191) + 128
                elif symbol[1] < 128:
                    symbol[1] = 191 - (128 - symbol[1])

            elif len(symbol) == 3:
                for index, byte in enumerate(symbol):
                    random.seed(self.seed)

                    if index == 0:
                        symbol[index] += random.randint(0, 15) # 239 - 224
                        if symbol[index] > 239:
                            symbol[index] = (symbol[index] - 239) + 224
                        elif symbol[index] < 224:
                            symbol[index] = 239 - (224 - symbol[index])

                    else:
                        symbol[index] += random.randint(0, 63) # 192 - 128
                        if symbol[index] > 191:
                            symbol[index] = (symbol[0] - 191) + 128
                        elif symbol[index] < 128:
                            symbol[index] = 191 - (128 - symbol[index])

            elif len(symbol) == 4:
                for index, byte in enumerate(symbol):
                    random.seed(self.seed)

                    if index == 0:
                        symbol[index] += random.randint(0, 7) # 247 - 240
                        if symbol[index] > 247:
                            symbol[index] = (symbol[index] - 247) + 240
                        elif symbol[index] < 240:
                            symbol[index] = 247 - (240 - symbol[index])

                    else:
                        symbol[index] += random.randint(0, 63) # 191 - 128
                        if symbol[index] > 191:
                            symbol[index] = (symbol[0] - 191) + 128
                        elif symbol[index] < 128:
                            symbol[index] = 191 - (128 - symbol[index])

            encrypt_message.append(bytes(symbol).decode('utf-8'))

        if not self.role:
            encrypt_message = self._shuffle(input_list=encrypt_message)

        return ''.join(encrypt_message)

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
obj.set_inputs(first_key='first', second_key='second', message='my message', role=0)
res = obj.encrypt()
print(res)

