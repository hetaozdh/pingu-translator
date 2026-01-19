from .vs import vs_to_byte
from .utils import bytes_to_codepoint
import zlib


def decode_bytes(pingu_text: str) -> bytes:
    vs_list = []
    for token in pingu_text.split():
        for ch in token:
            if ch != "n" and ch != "o" and ch != "t":
                vs_list.append(vs_to_byte(ch))
    return bytes(vs_list)


def decode(pingu_text: str) -> str:
    if pingu_text == "":
        return ""
    raw_bytes = decode_bytes(pingu_text)
    if not raw_bytes:
        return ""

    flag = raw_bytes[0]
    data = raw_bytes[1:]
    if flag == 1:
        data = zlib.decompress(data)

    chars = []
    i = 0
    while i < len(data):
        cp_bytes = data[i : i + 4]
        cp = bytes_to_codepoint(cp_bytes)
        chars.append(chr(cp))
        i += 4
    return "".join(chars)
