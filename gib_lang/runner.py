import logging
from typing import Callable, Optional

from .instruction import Instruction
from .tape import Tape, _TapeInitType
from .machine import Machine, _MachineInitType, MachineHeadError

logger = logging.getLogger("gib")


def run(
    machine: _MachineInitType,
    tape: _TapeInitType,
    max_steps: int = 100,
    callback: Optional[Callable[[Machine, Tape], bool]] = None,
) -> tuple[Machine, Tape]:
    """Run a Gibberish Language program on a tape"""
    machine = Machine(machine)
    tape = Tape(tape)
    try:
        while machine.steps < max_steps:
            if callback and callback(machine, tape):
                break
            instruction = machine.instruction
            current_bit = tape.get
            if instruction == Instruction.TOGGLE:
                tape.toggle()
                machine.move_right()
            elif instruction == Instruction.HEAD_RIGHT:
                tape.move_right()
                machine.move_right()
            elif instruction == Instruction.HEAD_LEFT:
                tape.move_left()
                machine.move_right()
            elif instruction == Instruction.LOOP_START:
                machine.loop_start(current_bit)
            elif instruction == Instruction.LOOP_END:
                machine.loop_end(current_bit)
            else:
                raise ValueError(f"Unknown instruction: {instruction}")

    except MachineHeadError:
        pass
    return machine, tape
