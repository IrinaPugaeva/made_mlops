import numpy as np

model_path = '../model/clf_pipeline.pickle'

model_name = 'logreg'

search_space = [{'clf__penalty': ['l1', 'l2'],
                'clf__C': [.01, .05, .1, .5, 1, 5, 10],
                'clf__solver': ['liblinear', 'saga']}] 

data_params = {
    'raw_data_path': '../data/raw/heart_cleveland_upload.csv',
    'test_size': 0.15,
    'random_state': 42,
    'train_data_path': '../data/raw/train.csv',
    'test_data_path': '../data/raw/oos.csv',
#     'scoring_data_path': '../data/scoring_data/data_april_2021.xlsx',
#     'path_to_result': '../data/scoring_results/results.xlsx'
}

