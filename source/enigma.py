class Engima:
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
        print(f"КОНФИГУРАЦИЯ ЭНИГМЫ\n"
              f"ПОЗИЦИИ РОТОРОВ A[{self.ra_pos}] B[{self.rb_pos}] C[{self.rc_pos}]\n"
              f"РОТОР A: {self.rotor_a}\n"
              f"РОТОР B: {self.rotor_b}\n"
              f"РОТОР C: {self.rotor_c}\n")

    def increment_rotors(self):
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
        return [self.ra_pos, self.rb_pos, self.rc_pos]

    def change_rotors_pos(self, ra: int, rb: int, rc: int):
        if (1 <= ra <= 26) and (1 <= rb < 26) and (1 <= rc <= 26):
            self.ra_pos = ra
            self.rb_pos = rb
            self.rc_pos = rc
            new_config = self.get_rotors_pos()
            print(f"Новая конфигурация роторов: А[{new_config[0]}] B[{new_config[1]}] C[{new_config[2]}]")
        else:
            print("Позиции роторов переданы некорректно. Конфигурация НЕ изменена")

    @staticmethod
    def get_rotor_letter(rotor:list, r_pos):
        return rotor[r_pos-1]

    def get_rotors_connection(self, input_char: str, reverse=False):
        # _ra = self.rotor_a
        # _rb = self.rotor_b
        # _rc = self.rotor_c
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
        converted_string = ""
        for letter in input_string:
            converted_string += self.get_rotors_connection(letter, reverse=reverse)["char"]
            self.increment_rotors()
        return converted_string


