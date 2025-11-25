
# attack_test_suite.py

from auto_pgd_config import AUTO_PGD_CONFIG
from square_attack_config import SQUARE_ATTACK_CONFIG

def print_auto_pgd_settings():
    print("Auto-PGD Attack Configuration:")
    for key, value in AUTO_PGD_CONFIG.items():
        print(f"{key}: {value}")

def print_square_attack_settings():
    print("Square Attack Configuration:")
    for key, value in SQUARE_ATTACK_CONFIG.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    print_auto_pgd_settings()
    print()
    print_square_attack_settings()
