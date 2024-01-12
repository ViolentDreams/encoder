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
        self.message = list(message)
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

        for index_symbol, symbol in enumerate(self.message):
            symbol = [byte for byte in symbol.encode('utf-8')]

            for index_byte, byte in reversed(list(enumerate(symbol))):
                random.seed(self.seed + index_symbol + index_byte)

                if index_byte == 0:

                    if len(symbol) == 1:

                        if not self.role:
                            symbol[index_byte] += random.randint(0, 127)
                            if symbol[index_byte] > 127:
                                symbol[index_byte] -= 127
                        else:
                            symbol[index_byte] -= random.randint(0, 127)
                            if symbol[index_byte] < 0:
                                symbol[index_byte] += 127

                    elif len(symbol) == 2:

                        if not self.role:
                            symbol[index_byte] += random.randint(0, 29)  # 223 - 194
                            if symbol[index_byte] > 223:
                                symbol[index_byte] = (symbol[index_byte] - 223) + 194
                            elif symbol[index_byte] < 194:
                                symbol[index_byte] = 223 - (194 - symbol[index_byte])
                        else:
                            symbol[index_byte] -= random.randint(0, 29)  # 223 - 194
                            if symbol[index_byte] > 223:
                                symbol[index_byte] = (symbol[index_byte] - 223) - 223
                            elif symbol[index_byte] < 194:
                                symbol[index_byte] = 223 - (194 - symbol[index_byte])

                    elif len(symbol) == 3:

                        if not self.role:
                            symbol[index_byte] += random.randint(0, 15)  # 239 - 224
                            if symbol[index_byte] > 239:
                                symbol[index_byte] = (symbol[index_byte] - 239) + 224
                            elif symbol[index_byte] < 224:
                                symbol[index_byte] = 239 - (224 - symbol[index_byte])
                        else:
                            symbol[index_byte] -= random.randint(0, 15)  # 239 - 224
                            if symbol[index_byte] > 239:
                                symbol[index_byte] = (symbol[index_byte] - 239) - 239
                            elif symbol[index_byte] < 224:
                                symbol[index_byte] = 239 - (224 - symbol[index_byte])

                    elif len(symbol) == 4:

                        if not self.role:
                            symbol[index_byte] += random.randint(0, 4)  # 244 - 240
                            if symbol[index_byte] > 244:
                                symbol[index_byte] = (symbol[index_byte] - 244) + 240
                            elif symbol[index_byte] < 240:
                                symbol[index_byte] = 244 - (240 - symbol[index_byte])
                        else:
                            symbol[index_byte] -= random.randint(0, 4)  # 247 - 240
                            if symbol[index_byte] > 244:
                                symbol[index_byte] = (symbol[index_byte] - 244) - 244
                            elif symbol[index_byte] < 240:
                                symbol[index_byte] = 244 - (240 - symbol[index_byte])

                else:

                    higher_border, lower_border = 191, 128

                    if len(symbol) == 3:
                        if symbol[0] == 224:
                            lower_border = 160
                        elif symbol[0] == 237:
                            higher_border = 159
                    elif len(symbol) == 4:
                        if symbol[0] == 240:
                            lower_border = 144
                        elif symbol[0] == 244:
                            higher_border = 143

                    if not self.role:
                        symbol[index_byte] += random.randint(0, higher_border - lower_border)  # 191 - 128
                        if symbol[index_byte] > higher_border:
                            symbol[index_byte] = (symbol[index_byte] - higher_border) + lower_border
                        elif symbol[index_byte] < lower_border:
                            symbol[index_byte] = higher_border - (lower_border - symbol[index_byte])
                    else:
                        symbol[index_byte] -= random.randint(0, higher_border - lower_border)  # 191 - 128
                        if symbol[index_byte] > higher_border:
                            symbol[index_byte] = (symbol[index_byte] - higher_border) - higher_border
                        elif symbol[index_byte] < lower_border:
                            symbol[index_byte] = higher_border - (lower_border - symbol[index_byte])

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
obj.set_inputs(first_key='first', second_key='second', message='Ư̴ŘŽԁى̵Ʈ͹ȚӞٻƖՆݖ܌ŗ!ɄI>̷թ٢', role=1)
res = obj.encrypt()
print(res)
