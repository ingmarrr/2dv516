import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def get_data(path: str) -> list[tuple[str, str, str]]:
    return [tuple(line.strip().split(",")) for line in read_file(path)]
