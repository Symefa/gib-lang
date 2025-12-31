from collections.abc import Sequence
from typing import Union, Optional, overload
import warnings

_TAPE_LENGHT = 8
_TapeInitType = Union[int, str, Sequence, "Tape"]


class Tape(Sequence[bool]):
    """Circular Tape"""

    _tape: list[bool]
    _head: int

    def __init__(
        self,
        tape: _TapeInitType = _TAPE_LENGHT,
        head: Optional[int] = None,
    ) -> None:
        if isinstance(tape, int):
            self._tape = [False] * tape
        elif isinstance(tape, str):
            self._tape = [bool(int(x)) for x in tape]
        elif isinstance(tape, Tape):
            self._tape = tape._tape.copy()
            if head is not None:
                warnings.warn(
                    "Head argument is ignored when initializing Tape with "
                    "another Tape. Set it to None to disable this warning.",
                    stacklevel=2,
                )
            head = tape._head
        elif isinstance(tape, Sequence):
            # Initialize the tape with the given sequence
            self._tape = [bool(x) for x in tape]
        else:
            raise TypeError("Tape must be initialized with an int or a sequence.")

        self._head = 0 if head is None else head

    @property
    def tape(self) -> Sequence[bool]:
        # Return a copy of the tape
        return list(self._tape)

    @property
    def get(self) -> bool:
        return self._tape[self._head]

    @property
    def head(self) -> int:
        return self._head

    def __len__(self) -> int:
        return len(self._tape)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tape):
            return self._tape == other._tape
        elif isinstance(other, str):
            return str(self) == other
        elif isinstance(other, Sequence):
            return self._tape == [bool(x) for x in other]
        else:
            return False

    @overload
    def __getitem__(self, index: int) -> bool: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[bool]: ...

    def __getitem__(
        self, index_or_slice: Union[int, slice]
    ) -> Union[bool, Sequence[bool]]:
        if isinstance(index_or_slice, (int, slice)):
            return self._tape[index_or_slice]
        else:
            raise TypeError("Index must be an int or a slice.")

    def _single_char_rp(self) -> str:
        return "".join("1" if bit else "0" for bit in self._tape)

    def __repr__(self) -> str:
        return f"Tape({self._single_char_rp()!r})"

    def __str__(self) -> str:
        return self._single_char_rp()

    def __hash__(self) -> int:
        return hash(str(self))

    def copy(self) -> "Tape":
        """Return a copy of the tape."""
        return Tape(self)

    def reset(self) -> None:
        """Reset the tape to all 0s and move the head to the start."""
        self._tape = [False] * len(self)
        self._head = 0

    def toggle(self) -> None:
        """Toggle the current cell."""
        self._tape[self._head] = not self._tape[self._head]

    def move_right(self, n: int = 1) -> None:
        """Move to the right."""
        self._head = (self._head + n) % len(self)

    def move_left(self, n: int = 1) -> None:
        """Move to the left."""
        self._head = (self._head - n) % len(self)

    def to_ascii(self) -> str:
        """Convert the tape to an ASCII string."""
        if len(self) % 8 != 0:
            raise ValueError("Tape length must be a multiple of 8 to convert to ASCII.")
        chars = []
        for i in range(0, len(self), 8):
            byte = self[i : i + 8]
            byte_str = "".join("1" if bit else "0" for bit in byte)
            chars.append(chr(int(byte_str, 2)))
        return "".join(chars)
