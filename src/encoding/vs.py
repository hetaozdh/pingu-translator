# Variation Selector ranges
VS_START = 0xFE00  # VS1  (0–15)
VS_EXT_START = 0xE0100  # VS17 (16–255)


def byte_to_vs(byte: int) -> str:
    """Map a byte (0–255) to a Unicode Variation Selector."""
    if not 0 <= byte <= 255:
        raise ValueError("byte out of range")

    if byte < 16:
        return chr(VS_START + byte)
    return chr(VS_EXT_START + (byte - 16))


def vs_to_byte(ch: str) -> int:
    """Map a Variation Selector back to a byte."""
    code = ord(ch)

    if VS_START <= code <= VS_START + 15:
        return code - VS_START

    if VS_EXT_START <= code <= VS_EXT_START + 239:
        return code - VS_EXT_START + 16

    raise ValueError("not a variation selector")
