from configuration import enigma_config

if __name__ == "__main__":
    rotors = list()
    for rotor_number in range(3):
        rotors.append(enigma_config.read_rotor(rotor_number))