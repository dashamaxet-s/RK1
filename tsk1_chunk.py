from typing import TypeVar

T = TypeVar('T')

def chunk(items: list[T], size: int) -> list[list[T]]:
    """Разбивает список на подсписки длиной не более size."""
    if size < 1:
        raise ValueError("size must be >= 1")
    return [items[i:i + size] for i in range(0, len(items), size)]