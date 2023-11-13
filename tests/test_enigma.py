import unittest
from source.enigma import Enigma  # Подставьте правильный путь к вашему классу

class TestEnigma(unittest.TestCase):
    def setUp(self):
        # Подготовка данных для тестов
        self.rotor_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.rotor_b = ['G', 'Q', 'W', 'F', 'M', 'D', 'A', 'Z', 'T', 'X', 'Y', 'S', 'E', 'U', 'V', 'P', 'B', 'R', 'L', 'I', 'N', 'O', 'C', 'J', 'K', 'H']
        self.rotor_c = ['R', 'Y', 'O', 'T', 'Z', 'P', 'K', 'S', 'Q', 'W', 'G', 'V', 'X', 'U', 'C', 'F', 'I', 'A', 'H', 'D', 'N', 'L', 'J', 'M', 'B', 'E']

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
        letter = self.enigma.get_rotor_letter(self.rotor_a, 3)
        self.assertEqual(letter, 'C')

    def test_convert(self):
        # Проверка кодирования строки
        encoded_string = self.enigma.convert('HELLO')
        self.assertEqual(encoded_string, 'HJSVD')

        # Проверка декодирования строки
        decoded_string = self.enigma.convert(encoded_string, reverse=True)
        self.assertEqual(decoded_string, 'HELLO')

if __name__ == '__main__':
    unittest.main()
