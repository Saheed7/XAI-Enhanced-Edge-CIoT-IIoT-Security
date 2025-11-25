
# square_attack_config.py

# Configuration for Square Attack

SQUARE_ATTACK_CONFIG = {
    'epsilon': 0.03,              # Perturbation budget
    'n_queries': 10000,           # Maximum number of queries
    'p_init': 0.8,                # Initial fraction of perturbed features
    'loss_fn': 'ce',              # Loss function: 'ce' = cross-entropy
    'targeted': False,            # Whether attack is targeted
    'seed': 42                    # Random seed
}
