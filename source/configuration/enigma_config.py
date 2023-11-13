from pathlib import Path


def read_rotor(rotor_number: int) -> list:
    if not (1 <= rotor_number <= 4):
        return []
    _rotor_file_name = f"rotor{rotor_number}.txt"
    _rotor_path = Path(Path.cwd(), "configuration", _rotor_file_name)
    _rotor_config = []
    with open(_rotor_path, "r") as rotor:
        _rotor_config = rotor.read().strip()

    return _rotor_config
