from pathlib import Path


def read_rotor(rotor_number: int) -> list:
    """Прочитать конфигурацию ротора

    Args:
        rotor_number (int): номер ротора для считывания

    Returns:
        list: Список содержащий порядок букв на роторе
    """
    if not (1 <= rotor_number <= 5):
        return []
    _rotor_file_name = f"rotor{rotor_number}.txt"
    _rotor_path = Path(Path.cwd(), "configuration", _rotor_file_name)
    _rotor_config = []
    with open(_rotor_path, "r") as rotor:
        _rotor_config = rotor.read().strip()

    return _rotor_config
