from collections.abc import Sequence

from typing import Union, Optional, overload
import warnings

from .instruction import Instruction
from .exceptions import MachineHeadError, InvalidInstructionError

_MachineInitType = Union[str, Sequence[Instruction], "Machine"]


class Machine(Sequence[Instruction]):
    """Gibberish Language Machine based on RBF"""

    _machine: list[Instruction]
    _head: int
    _steps: int

    def __init__(
        self,
        machine: _MachineInitType,
        head: Optional[int] = None,
    ) -> None:
        if isinstance(machine, Machine):
            self._machine = list(machine.machine)
            self._head = machine.head
            self._steps = machine.steps
            if head is not None:
                warnings.warn(
                    "head parameter is ignored when initializing from another Machine instance",
                    stacklevel=2,
                )
        elif isinstance(machine, (str, Sequence)):
            validated_machine = validate_machine(machine)
            self._machine = validated_machine
            head = 0 if head is None else head
            self._head = head
            self._steps = 0
        else:
            raise TypeError(
                "Machine must be initialized with a string, a sequence of Instructions, or another Machine instance"
            )

    @property
    def machine(self) -> Sequence[Instruction]:
        """returns a copy of the machine's instructions"""
        return self._machine.copy()

    @property
    def head(self) -> int:
        """returns the current head position"""
        return self._head

    @property
    def steps(self) -> int:
        """returns the number of steps taken"""
        return self._steps

    @property
    def instruction(self) -> Instruction:
        if len(self) == 0:
            raise MachineHeadError("Machine is empty")
        return self._machine[self._head]

    def __len__(self) -> int:
        return len(self._machine)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Machine):
            return self._machine == other.machine
        elif isinstance(other, str):
            return str(self) == other
        else:
            return False

    @overload
    def __getitem__(self, index: int) -> Instruction: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[Instruction]: ...

    def __getitem__(
        self,
        index_or_slice: Union[int, slice],
    ) -> Union[Instruction, Sequence[Instruction]]:
        if isinstance(index_or_slice, (int, slice)):
            return self._machine[index_or_slice]
        else:
            raise TypeError("Index must be an integer or a slice")

    def _single_char_rp(self) -> str:
        return "".join(instruction.value for instruction in self._machine)

    def __repr__(self) -> str:
        return f"Machine({self._single_char_rp()!r})"

    def __str__(self) -> str:
        return self._single_char_rp()

    def __hash__(self) -> int:
        return hash(str(self))

    def copy(self) -> "Machine":
        return Machine(self)

    def restart(self) -> None:
        self._head = 0
        self._steps = 0

    def _move_right(self) -> None:
        if self._head < len(self) - 1:
            self._head += 1
        else:
            raise MachineHeadError("Machine head overflow")

    def move_right(self, n: int = 1) -> None:
        for _ in range(n):
            self._steps += 1
            self._move_right()

    def _move_left(self) -> None:
        if self._head > 0:
            self._head -= 1
        else:
            raise MachineHeadError("Machine head underflow")

    def move_left(self, n: int = 1) -> None:
        for _ in range(n):
            self._steps += 1
            self._move_left()

    def loop_start(self, current_bit: bool) -> None:
        if self.instruction != Instruction.HEAD_LEFT_LOOP_START:
            raise ValueError("Not at a loop start.")

        self._steps += 1
        
        if not current_bit:
            try:
                bracket_depth = 1
                while bracket_depth > 0:
                    self._move_right()
                    if self.instruction == Instruction.HEAD_LEFT_LOOP_START:
                        bracket_depth += 1
                    elif self.instruction == Instruction.LOOP_END:
                        bracket_depth -= 1

            except MachineHeadError:
                raise InvalidInstructionError("Unmatched loop start.") from None

        try:
            self._move_right()
        except MachineHeadError:
            raise

    def loop_end(self, current_bit: bool) -> None:
        if self.instruction != Instruction.LOOP_END:
            raise ValueError("Not at a loop end.")

        self._steps += 1

        if not current_bit:
            try:
                bracket_depth = 1
                while bracket_depth > 0:
                    self._move_left()
                    if self._machine[self._head] == Instruction.HEAD_LEFT_LOOP_START:
                        bracket_depth -= 1
                    elif self._machine[self._head] == Instruction.LOOP_END:
                        bracket_depth += 1

            except MachineHeadError:
                raise InvalidInstructionError("Unmatched loop end.") from None
        self._move_right()

def _chunk_string(s, n):
    return (s[i:i+n] for i in range(0, len(s), n))

def validate_machine(machine: Union[str, Sequence[Instruction]]) -> list[Instruction]:
    valid_instructions: Sequence[Instruction]
    if isinstance(machine, str):
        try:

            valid_instructions = [Instruction(instruction) for instruction in _chunk_string(machine, 8)]
        except ValueError as e:
            raise InvalidInstructionError(str(e)) from None
    else:
        valid_instructions = list(machine)

    depth = 0
    for instruction in valid_instructions:
        if instruction == Instruction.HEAD_LEFT_LOOP_START:
            depth += 1
        elif instruction == Instruction.LOOP_END:
            depth -= 1

        if depth < 0:
            raise InvalidInstructionError(
                "Invalid instruction sequence: unexpected FAFAFUFU"
            )
    if depth != 0:
        raise InvalidInstructionError(
            "Invalid instruction sequence: unmatched FUFUFAFA "
        )

    return valid_instructions
