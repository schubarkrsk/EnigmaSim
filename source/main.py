from configuration import enigma_config
from enigma import Enigma

# import re

if __name__ == "__main__":
    rotors = []
    for rotor_number in range(1, 4, 1):
        rotors.append(enigma_config.read_rotor(rotor_number))

    enigma = Enigma(rotors[0], rotors[1], rotors[2])
    enigma.state()

    while True:
        print("[1] - ЗАКОДИРОВАТЬ\n"
              "[2] - РАСКОДИРОВАТЬ\n"
              "[3] - СМЕНИТЬ ПОЗИЦИЮ РОТОРА\n"
              "[4] - ТЕКУЩИЙ СТАТУС ЭНИГМЫ\n"
              "[НЕ цифра] - ВЫХОД")
        try:
            answer = int(input(">>>"))
        except Exception:
            raise SystemExit

        match answer:
            case 1:
                message = input("ТЕКСТ НА АНГЛИЙСКОМ БЕЗ ПРОБЕЛОВ >>> ").upper()
                print(enigma.convert(message, reverse=False))

            case 2:
                message = input("ТЕКСТ НА АНГЛИЙСКОМ БЕЗ ПРОБЕЛОВ >>> ").upper()
                decoded_text = enigma.convert(message, reverse=True)
                # words = re.findall('[A-Z]+[a-z]*', decoded_text)
                # result = ' '.join(words) # TODO : make words separating
                print(decoded_text)

            case 3:
                rotors_pos = enigma.get_rotors_pos()
                print(f"ТЕКУЩИЕ ПОЗИЦИИ РОТОРОВ [A:{rotors_pos[0]}, B:{rotors_pos[1]}, C:{rotors_pos[2]}]")
                a_pos = int(input("ПОЗИЦИЯ РОТОРА A >>> "))
                b_pos = int(input("ПОЗИЦИЯ РОТОРА B >>> "))
                c_pos = int(input("ПОЗИЦИЯ РОТОРА C >>> "))
                enigma.change_rotors_pos(a_pos, b_pos, c_pos)
            case 4:
                enigma.state()

        rotors_pos = enigma.get_rotors_pos()
        print(f"ПОЗИЦИИ РОТОРОВ ПОСЛЕ ОПЕРАЦИИ [A:{rotors_pos[0]}, B:{rotors_pos[1]}, C:{rotors_pos[2]}]")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
