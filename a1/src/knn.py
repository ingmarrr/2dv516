from dataclasses import dataclass
import enum
import numpy as np
import numpy.typing as npt
import typing


class Status(enum.Enum):
    Ok = 1
    Fail = 0
    Undefined = -1


pty = np.dtype([("x", float), ("y", float), ("status", Status)])


@dataclass
class Point:
    x: float
    y: float
    status: Status

    def __init__(self, x: float, y: float, status: Status = Status.Undefined) -> None:
        self.x = x
        self.y = y
        self.status = status

    def distance_to(self, other: "Point") -> float:
        # print("Distance to: ")
        # print(other)
        # print(type(other))
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def nearest_points(self, data: np.ndarray, k: int) -> np.ndarray:

        distances = np.zeros((len(data),))
        for i in range(len(data)):
            distances[i] = self.distance_to(data[i])

        indices = np.argsort(distances)[:k]
        return data[indices]
        # # print("Nearest points: ")
        # # print(data)
        # points: np.ndarray = np.ndarray(shape=(k,), dtype=Point)

        # # print(points)
        # return points

    def with_status(self, status: bool) -> "Point":
        return Point(self.x, self.y, Status.Ok if status else Status.Fail)

    def __str__(self) -> str:
        return f"Point=({self.x}, {self.y}, {'1' if self.status == Status.Ok else '0'})"


def get_points(path: str) -> np.ndarray:
    data: np.ndarray = np.loadtxt(path, delimiter=",", dtype=float)
    lines: np.ndarray = np.ndarray(shape=(data.shape[0],), dtype=pty)

    for i, line in enumerate(data):
        lines[i] = (line[0], line[1], Status.Ok if line[2] == 1 else Status.Fail)

    return np.vectorize(lambda l: Point(*l), otypes=[Point])(lines)


def is_ok(point: Point, data: np.ndarray, k: int = 3) -> bool:
    # print("Is ok: ")
    # print(data)
    nearest = point.nearest_points(data, k)
    return sum([1 if p.status == Status.Ok else 0 for p in nearest]) >= k / 2


def main():
    ps = get_points("A1_datasets/microchips.csv")
    print(ps)


if __name__ == "__main__":
    main()
