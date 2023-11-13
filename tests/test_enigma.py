import unittest
from source.enigma import Enigma  # Подставьте правильный путь к вашему классу


class TestEnigma(unittest.TestCase):
    def setUp(self):
        # Подготовка данных для тестов
        self.rotor_a = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S',
                        'P', 'A', 'I', 'B', 'R', 'C', 'J']
        self.rotor_b = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z',
                        'N', 'P', 'Y', 'F', 'V', 'O', 'E']
        self.rotor_c = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G',
                        'A', 'K', 'M', 'U', 'S', 'Q', 'O']

        self.enigma = Enigma(self.rotor_a, self.rotor_b, self.rotor_c)

    def test_get_rotors_pos(self):
        # Проверка получения позиций роторов при стандартном запуске
        positions = self.enigma.get_rotors_pos()
        self.assertEqual(positions, [1, 1, 1])

    def test_change_rotors_pos(self):
        # Проверка изменения позиций роторов
        self.enigma.change_rotors_pos(5, 10, 15)
        positions = self.enigma.get_rotors_pos()
        self.assertEqual(positions, [5, 10, 15])

    def test_get_rotor_letter(self):
        # Проверка получения буквы из ротора
        self.enigma.change_rotors_pos(1,1,1)
        letter = self.enigma.get_rotor_letter(self.rotor_a, 3)
        self.assertEqual(letter, 'M')

    def test_convert(self):
        # Проверка кодирования строки
        encoded_string = self.enigma.convert('HELLO')
        self.assertEqual(encoded_string, 'CKBQL')

        # Проверка декодирования строки
        self.enigma.change_rotors_pos(1, 1, 1)
        decoded_string = self.enigma.convert(encoded_string, reverse=True)
        self.assertEqual(decoded_string, 'HELLO')


if __name__ == '__main__':
    unittest.main()
