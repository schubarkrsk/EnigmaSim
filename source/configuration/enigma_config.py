from pathlib import Path


def read_rotor(rotor_number: int) -> list:
    if 1 > rotor_number > 4:
        return []
    _rotor_file_name = f"rotor{rotor_number}.txt"
    _rotor_path = Path(Path.cwd(), _rotor_file_name)
    with open(_rotor_path, "r") as rotor:
        _rotor_config = [line.strip().split() for line in rotor]

    return _rotor_config
