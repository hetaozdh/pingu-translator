import random
import zlib
from typing import Iterator
from .vs import byte_to_vs
from .utils import codepoint_to_bytes


def encode_bytes(data: bytes) -> str:
    if len(data) < 4:
        raise ValueError("data too short to encode")
    num_bytes = len(data)
    lengths_of_noots = []
    random.seed(num_bytes + len(list(filter(lambda b: b > 128, list(data)))))

    while sum(lengths_of_noots) < num_bytes:
        lengths_of_noots.append(random.randint(4, 20))

    while sum(lengths_of_noots) > num_bytes:
        reducible = [i for i, v in enumerate(lengths_of_noots) if v > 4]
        if not reducible:
            lengths_of_noots.pop()
            lengths_of_noots[random.randint(0, len(lengths_of_noots) - 1)] += (
                num_bytes - sum(lengths_of_noots)
            )
            continue
        i = random.choice(reducible)
        lengths_of_noots[i] -= 1

    vs_iter: Iterator[str] = map(byte_to_vs, data)
    tokens = []
    for length in lengths_of_noots:
        out = []
        for i in range(length):
            carrier = "n" if i == 0 else "t" if i == length - 1 else "o"
            out.append(carrier + next(vs_iter))
        tokens.append("".join(out))
    return " ".join(tokens)


def compress_encode(data: bytes) -> str:
    compressed = zlib.compress(data, level=9)
    return encode_bytes(bytes([1]) + compressed)


def encode_raw(data: bytes) -> str:
    return encode_bytes(bytes([0]) + data)


def encode(text: str) -> str:
    if text == "":
        return ""
    data = b"".join(codepoint_to_bytes(ord(ch)) for ch in text)
    if len(data) < 12:
        return encode_raw(data)
    else:
        return compress_encode(data)
