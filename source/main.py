from configuration import enigma_config
from enigma import Engima

if __name__ == "__main__":
    rotors = []
    for rotor_number in range(1, 4, 1):
        rotors.append(enigma_config.read_rotor(rotor_number))

    enigma = Engima(rotors[0], rotors[1], rotors[2])
    enigma.state()

    while True:
        print("[1] - encode message\n"
              "[2] - decode message\n"
              "[3] - set rotors position\n"
              "[4] - enigma state info\n"
              "[Any letter key] - Quit")
        try:
            answ = int(input(">>>"))
        except Exception:
            raise SystemExit

        match answ:
            case 1:
                message = input("YOUR MESSAGE (WITHOUT SPACES) >>> ").upper()
                print(enigma.convert(message, reverse=False))
            case 2:
                message = input("YOUR MESSAGE (WITHOUT SPACES) >>> ").upper()
                print(enigma.convert(message, reverse=True))
            case 3:
                rotors_pos = enigma.get_rotors_pos()
                print(f"CURRENT ROTORS POS [{rotors_pos[0]}, {rotors_pos[1]}, {rotors_pos[2]}]")
                a_pos = int(input("Position for A rotor >>> "))
                b_pos = int(input("Position for B rotor >>> "))
                c_pos = int(input("Position for C rotor >>> "))
                enigma.change_rotors_pos(a_pos, b_pos, c_pos)
            case 4:
                enigma.state()
