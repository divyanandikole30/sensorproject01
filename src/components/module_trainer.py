import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

from xgoost import XGBClassifier
from sklearn.svm import RandomClassifier,GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV,train_test_split
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils

from dataclasses import dataclass


@dataclass
class ModelTrainerConfig:
    artifact_folder=os.path.join(artifact_folder)
    trained_model_path=os.path.join(artifact_folder,"model.pkl")
    expected_accuracy=0.45
    model_config_file_path=os.path.join('config','model.yaml')
    