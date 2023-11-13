from pathlib import Path
from typing import List, Any


def read_rotor(rotor_number: int) -> list[Any] | str:
    """Прочитать конфигурацию ротора

    Args:
        rotor_number (int): номер ротора для считывания

    Returns:
        list: Список содержащий порядок букв на роторе
    """
    if not (1 <= rotor_number <= 5):
        return []
    rotor_file_name = f"rotor{rotor_number}.txt"
    rotor_path = Path(Path.cwd(), "configuration", rotor_file_name)
    rotor_config = []
    with open(rotor_path, "r") as rotor:
        rotor_config = rotor.read().strip()

    return rotor_config
