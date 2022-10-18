import os

for root, dirs, files in os.walk(r'results\dense\2022_10_17_pqsar_olea_hyperopt_seed_2'):
    for file in files:
        if file.endswith('optuna_params.json'):
            print(os.path.join(root,file))