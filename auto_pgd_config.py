
# auto_pgd_config.py

# Configuration for Auto-PGD attack

AUTO_PGD_CONFIG = {
    'epsilon': 0.03,          # Perturbation limit
    'num_steps': 20,          # Number of iterations
    'step_size': 0.01,        # Step size for each iteration
    'norm': 'Linf',           # Norm type (Linf or L2)
    'random_start': True,     # Whether to use random initialization
    'loss_fn': 'ce',          # Loss function: 'ce' = cross-entropy, 'dlr' = difference of logits ratio
    'targeted': False,        # Whether the attack is targeted
    'seed': 42                # Random seed for reproducibility
}
