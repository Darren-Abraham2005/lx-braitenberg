from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.ones(shape=shape, dtype="float32")*(-0.25)
    # TODO define left matrix
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.ones(shape=shape, dtype="float32")*(0.25)
    # TODO define right matrix
    return res
