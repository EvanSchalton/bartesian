from typing import TypedDict


class TrainingData(TypedDict):
    filename: str
    input: list[int]
    output: list[list[float]]
