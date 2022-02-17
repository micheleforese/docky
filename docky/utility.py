import hashlib


def hash(source: str) -> str:
    return hashlib.sha1(source.encode())
