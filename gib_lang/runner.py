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
            if instruction == Instruction.TOGGLE_HEAD_RIGHT:
                tape.toggle()
                tape.move_right()
                machine.move_right()
            elif instruction == Instruction.HEAD_LEFT_LOOP_START:
                tape.move_left()
                current_bit = tape.get
                logger.debug(f"Loop start at head {machine.head}, current bit: {current_bit}")
                machine.loop_start(current_bit)
            elif instruction == Instruction.LOOP_END:
                logger.debug(f"Loop end at head {machine.head}, current bit: {current_bit}")
                machine.loop_end(current_bit)
            elif instruction == Instruction.NO_OP:
                machine.move_right()
            else:
                raise ValueError(f"Unknown instruction: {instruction}")

    except MachineHeadError:
        pass
    return machine, tape
