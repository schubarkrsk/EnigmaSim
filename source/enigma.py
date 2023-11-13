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

    ra_pos = 1
    rb_pos = 1
    rc_pos = 1

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
              f"ПОЗИЦИИ РОТОРОВ A[{self.ra_pos}] B[{self.rb_pos}] C[{self.rc_pos}]\n"
              f"РОТОР A: {self.rotor_a}\n"
              f"РОТОР B: {self.rotor_b}\n"
              f"РОТОР C: {self.rotor_c}\n")

    def increment_rotors(self):
        """Увеличение заначения позиции роторов."""
        self.ra_pos += 1
        if self.ra_pos > 26:
            self.ra_pos = 1

            self.rb_pos += 1
            if self.rb_pos > 26:
                self.rb_pos = 1

                self.rc_pos += 1
                if self.rc_pos > 26:
                    self.rc_pos = 1

    def get_rotors_pos(self) -> list:
        """Получение позиций роторов.

        Returns:
            list: список содержащий текущие позиции роторов
        """
        return [self.ra_pos, self.rb_pos, self.rc_pos]

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
            self.ra_pos = ra
            self.rb_pos = rb
            self.rc_pos = rc
            new_config = self.get_rotors_pos()
            print(f"Новая конфигурация роторов: А[{new_config[0]}] B[{new_config[1]}] C[{new_config[2]}]")
        else:
            print("Позиции роторов переданы некорректно. Конфигурация НЕ изменена")

    @staticmethod
    def get_rotor_letter(rotor:list, r_pos:int):
        """Получить букву на роторе при определенной позиции.

        Args:
            rotor (list): Конфигурация ротора
            r_pos (int): Номер позиции

        Returns:
            str: Буква стоящая на позици r_pos в роторе rotor
        """
        return rotor[r_pos-1]

    def get_rotors_connection(self, input_char: str, reverse=False)->dict:
        """Получить букву после прохождения через блок роторов.


        Args:
            input_char (str): Буква, которая будет пропущена через роторы.
            reverse (bool, optional): Если True - будет произведено дешифрование

        Returns:
            dict: Словарь содержащий букву и ее индекс на последнем роторе
        """
        _ra = self.rotor_a[self.ra_pos:] + self.rotor_a[:self.ra_pos]
        _rb = self.rotor_b[self.rb_pos:] + self.rotor_b[:self.rb_pos]
        _rc = self.rotor_c[self.rc_pos:] + self.rotor_c[:self.rc_pos]

        result = {
            "char": "",
            "index": 0,
        }

        if not reverse:
            # Находим индекс в роторе A, с учетом позиции ротора
            ra_i = (_ra.index(input_char) - self.ra_pos) % 26
            rb_i = (_rb.index(_ra[ra_i]) - self.rb_pos) % 26
            rc_i = (_rc.index(_rb[rb_i]) - self.rc_pos) % 26

            result["char"] = _rc[rc_i]
            result["index"] = rc_i

        if reverse:
            # Для декодирования нужно пройти обратный путь по роторам
            rc_i = (_rc.index(input_char) + self.rc_pos) % 26
            rb_i = (_rb.index(_rc[rc_i]) + self.rb_pos) % 26
            ra_i = (_ra.index(_rb[rb_i]) + self.ra_pos) % 26

            result["char"] = _ra[ra_i]
            result["index"] = ra_i

        return result

    def convert(self, input_string:str, reverse=False)->str:
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


