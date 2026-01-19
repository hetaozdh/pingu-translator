def codepoint_to_bytes(cp: int) -> bytes:
    """Unicode code point → 4-byte big-endian."""
    return cp.to_bytes(4, byteorder="big")


def bytes_to_codepoint(b: bytes) -> int:
    """4-byte big-endian → Unicode code point."""
    if len(b) != 4:
        raise ValueError("invalid byte length")
    return int.from_bytes(b, byteorder="big")
