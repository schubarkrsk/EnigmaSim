class Enigma:
    """Класс эмуляции шифровальной машины Энигма
    
    Args:
        rotor_a (list): Конфигурация для ротора A.
        rotor_b (list): Конфигурация для ротора B.
        rotor_c (list): Конфигурация для ротора C.
        plugs (list, optional): Конфигурация переставления букв.
        
    Attributes:
        ra_pos (int): Позиция ротора A.
        rb_pos (int): Позиция ротора B.
        rc_pos (int): Позиция ротора C.

    Methods:
        state(): Отображает текущее состояние Энигмы.
        increment_rotors(): Увеличение заначения позиции роторов.
        get_rotors_pos(): Получение позиций роторов.
        change_rotors_pos(ra: int, rb: int, rc: int): Изменить позиции роторов.
        get_rotor_letter(rotor: list, r_pos: int): Получить букву на роторе при определенной позиции.
        get_rotors_connection(input_char: str, reverse: bool): Получить букву после прохождения через блок роторов.
        convert(input_string: str, reverse: bool): Зашифровать или дешифровать сообщение
    """

    rotor_a_pos = 1
    rotor_b_pos = 1
    rotor_c_pos = 1

    def __init__(self, rotor_a: list, rotor_b: list, rotor_c: list, plugs=None):
        if plugs is None:
            plugs = []
        self.rotor_a = rotor_a
        self.rotor_b = rotor_b
        self.rotor_c = rotor_c
        self.plugs = plugs

    def state(self):
        """Отображает текущее состояние Энигмы."""
        print(f"КОНФИГУРАЦИЯ ЭНИГМЫ\n"
              f"ПОЗИЦИИ РОТОРОВ A[{self.rotor_a_pos}] B[{self.rotor_b_pos}] C[{self.rotor_c_pos}]\n"
              f"РОТОР A: {self.rotor_a}\n"
              f"РОТОР B: {self.rotor_b}\n"
              f"РОТОР C: {self.rotor_c}\n")

    def increment_rotors(self):
        """Увеличение заначения позиции роторов."""
        self.rotor_a_pos += 1
        if self.rotor_a_pos > 26:
            self.rotor_a_pos = 1

            self.rotor_b_pos += 1
            if self.rotor_b_pos > 26:
                self.rotor_b_pos = 1

                self.rotor_c_pos += 1
                if self.rotor_c_pos > 26:
                    self.rotor_c_pos = 1

    def get_rotors_pos(self) -> list:
        """Получение позиций роторов.

        Returns:
            list: список содержащий текущие позиции роторов
        """
        return [self.rotor_a_pos, self.rotor_b_pos, self.rotor_c_pos]

    def change_rotors_pos(self, ra: int, rb: int, rc: int):
        """Изменить позиции роторов

            Args:
                ra (int): Новая позиция ротора A.
                rb (int): Новая позиция ротора B.
                rc (int): Новая позиция ротора C.

            Prints:
                str: Информация о новых позициях роторов
            """
        if (1 <= ra <= 26) and (1 <= rb < 26) and (1 <= rc <= 26):
            self.rotor_a_pos = ra
            self.rotor_b_pos = rb
            self.rotor_c_pos = rc
            new_config = self.get_rotors_pos()
            print(f"Новая конфигурация роторов: А[{new_config[0]}] B[{new_config[1]}] C[{new_config[2]}]")
        else:
            print("Позиции роторов переданы некорректно. Конфигурация НЕ изменена")

    @staticmethod
    def get_rotor_letter(rotor: list, r_pos: int):
        """Получить букву на роторе при определенной позиции.

        Args:
            rotor (list): Конфигурация ротора
            r_pos (int): Номер позиции

        Returns:
            str: Буква стоящая на позици r_pos в роторе rotor
        """
        return rotor[r_pos - 1]

    def get_rotors_connection(self, input_char: str, reverse=False) -> dict:
        """Получить букву после прохождения через блок роторов.


        Args:
            input_char (str): Буква, которая будет пропущена через роторы
            reverse (bool, optional): Если True - будет произведено дешифрование

        Returns:
            dict: Словарь содержащий букву и ее индекс на последнем роторе
        """
        rotor_a_shift = self.rotor_a[self.rotor_a_pos:] + self.rotor_a[:self.rotor_a_pos]
        rotor_b_shift = self.rotor_b[self.rotor_b_pos:] + self.rotor_b[:self.rotor_b_pos]
        rotor_c_shift = self.rotor_c[self.rotor_c_pos:] + self.rotor_c[:self.rotor_c_pos]

        result = {
            "char": "",
            "index": 0,
        }

        if not reverse:
            # Находим индекс в роторе A, с учетом позиции ротора
            rotor_a_index = (rotor_a_shift.index(input_char) - self.rotor_a_pos) % 26
            rotor_b_index = (rotor_b_shift.index(rotor_a_shift[rotor_a_index]) - self.rotor_b_pos) % 26
            rotor_c_index = (rotor_c_shift.index(rotor_b_shift[rotor_b_index]) - self.rotor_c_pos) % 26

            result["char"] = rotor_c_shift[rotor_c_index]
            result["index"] = rotor_c_index

        if reverse:
            # Для декодирования нужно пройти обратный путь по роторам
            rotor_c_index = (rotor_c_shift.index(input_char) + self.rotor_c_pos) % 26
            rotor_b_index = (rotor_b_shift.index(rotor_c_shift[rotor_c_index]) + self.rotor_b_pos) % 26
            rotor_a_index = (rotor_a_shift.index(rotor_b_shift[rotor_b_index]) + self.rotor_a_pos) % 26

            result["char"] = rotor_a_shift[rotor_a_index]
            result["index"] = rotor_a_index

        return result

    def convert(self, input_string: str, reverse=False) -> str:
        """Зашифровать или дешифровать строку с помощью Энигмы

        Args:
            input_string (str): Входящая строка
            reverse (bool, optional): Если True - идет расшифровка

        Returns:
            str: Преобразованная строка
        """
        converted_string = ""
        for letter in input_string:
            converted_string += self.get_rotors_connection(letter, reverse=reverse)["char"]
            self.increment_rotors()
        return converted_string
