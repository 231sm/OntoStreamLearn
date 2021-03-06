# -*- coding: utf-8 -*-
"""define all global parameters here."""
from os.path import join

WEIGHT = 0
BOE = 0
"""system part."""
WORK_DIRECTORY = ""
DATA_DIRECTORY = ""
DATA_INPUT_DIRECTORY = join(DATA_DIRECTORY, "input")
DATA_OUTPUT_DIRECTORY = join(DATA_DIRECTORY, "output")
SEMI_RESULT_DIRECTORY = join(DATA_DIRECTORY, "semi-result")
TRAINING_DIRECTORY = join(DATA_DIRECTORY, "output", "training")
BASELINE_DIRECTORY = join(DATA_DIRECTORY, "output", "baseline")
RECORD_DIRECTORY = join(WORK_DIRECTORY, "record", "log.txt")
PARAMETER_DIRECTORY = join(WORK_DIRECTORY, "settings", "parameters.py")
"""tensorflow configuration."""
ALLOW_SOFT_PLACEMENT = True
LOG_DEVICE_PLACEMENT = False
"""machine learning model."""
DEBUG = True
SEED = 42
SEED_MAX = 1000
NUM_CHANNELS = 1
NUM_CLASSES = 391
TRAIN_RATIO = 0.8
VALIDATION_RATIO = 0.1
BATCH_SIZE = 4
MAX_EPOCHS = 1000
LEARNING_RATE = 0.0001
DECAY_RATE = 0.95
L2_REGULARIZATION_LAMBDA = 5e-4
DROPOUT_RATE = 0.5
EVALUATE_EVERY = 100
CHECKPOINT_EVERY = 100
CHECKPOINT_DIRECTORY = TRAINING_DIRECTORY
EARLY_STOPPING = 2
FORCE_RM_RECORD = False
"""time series."""
CONTINUOUS_WINDOW = 200
DISCRETE_WINDOW = 391
# DISCRETE_WINDOW = 1
CONTINUOUS_MODELS = ["LinearRegression", "CNN"]
DISCRETE_MODELS = ["LSTM"]
MIXTURE_MODELS = ["MixNN"]
"""cnn."""
FILTER_SIZES = [2, 3, 4, 5]
NUM_FILTERS = [128, 128, 128, 128]
SIZE_WORDVEC = 200
NUM_WORDS = 706
"""rnn."""
FORGET_GATE_BIASES = 0.0
NUM_LAYERS = 1
HIDDEN_DIM = 100
NUM_INPUT = 500
# NUM_INPUT = 500 + 423
NUM_OUTPUT = 391
# NUM_OUTPUT = 1
