import numpy as np
from src.knn import Point, get_points
import src


def main():
    point: Point = Point(1, 2)
    data = get_points("./A1_datasets/microchips.csv")
    nearest = point.nearest_points(data, src.K)
    print(nearest)


if __name__ == "__main__":
    main()
