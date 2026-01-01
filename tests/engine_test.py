import pytest

from gib_lang import Machine, transpile, run
from gib_lang.machine import Instruction, MachineHeadError, InvalidInstructionError


# """
# FAFAFAFA FUFUFAFA FAFAFUFU                                   #toggle
# FAFAFAFA FUFUFAFA FAFAFUFU FAFAFAFA                          #move right
# FUFUFAFA FAFAFUFU                                            #move left
# FAFAFAFA FUFUFAFA FAFAFUFU FAFAFAFA FUFUFAFA                 #loop start
# FAFAFUFU                                                     #loop end

# """
# @pytest.fixture
# def forward() -> Machine:
#     instruction = "*>*"
#     return Machine(instruction)

# def backward() -> Machine:
#     instruction = "*<*"
#     return Machine(instruction)

# def forward_check(forward: Machine) -> None:
#     machine, tape = run(forward, "100")
    
#     assert machine.steps == 100
#     assert tape == "010"
    
#     machine.restart()
    
#     machine, tape = run(machine, tape)
    
#     assert machine.steps == 100
#     assert tape == "001"
    
# def backward_check(backward: Machine) -> None:
#     machine, tape = run(backward, "100")
    
#     assert machine.steps == 100
#     assert tape == "010"
    
#     machine.restart()
    
#     machine, tape = run(machine, tape)
    
#     assert machine.steps == 100
#     assert tape == "100"

# def test_drive() -> None:
#     source = "*>"*8
#     machine = Machine(source)

#     assert machine == source

# def test_hash() -> None:
#     source = "*>"*8
#     machine = Machine(source)
    
#     assert hash(machine) == hash(source)

# def test_eq() -> None:
#     source = "*>"*8
#     machine = Machine(source)
#     machine2 = Machine(source)
#     assert machine == machine2

# def test_copy() -> None:
#     source = "*>"*8
#     machine = Machine(source)
#     machine2 = machine.copy()
#     assert machine == machine2

# def test_invalid_instruction() -> None:
#     source = "*)"
#     with pytest.raises(InvalidInstructionError):
#          Machine(source)
    

# def test_head() -> None:
#     source = "*>"*8
#     machine = Machine(source)

#     assert len(machine) == 16
#     assert machine.head == 0

#     for i in range(15):
#         assert machine.head == i
#         machine.move_right()
    
#     assert machine.steps == 15

#     assert machine.head == 15
#     with pytest.raises(MachineHeadError):
#         machine.move_right()
    
#     assert machine.head == 15
#     assert machine.steps == 16

#     for i in range(15, 0, -1):
#         assert machine.head == i
#         machine.move_left()
#     assert machine.head == 0
#     assert machine.steps == 31
#     with pytest.raises(MachineHeadError):
#         machine.move_left()
#     assert machine.head == 0
#     assert machine.steps == 32

# def test_restart() -> None:
#     source = "*>"*8
#     machine = Machine(source)

#     machine.move_right(8)
    
#     assert machine.head == 8
#     assert machine.steps == 8

#     machine.restart()

#     assert machine.head == 0
#     assert machine.steps == 0

# def test_getitem() -> None:
#     source = "*>"*8
#     machine = Machine(source)

#     assert machine[0] == Instruction.TOGGLE
#     assert machine[1] == Instruction.HEAD_RIGHT
#     assert machine[2] == Instruction.TOGGLE

# def test_instruction_prop() -> None:
#     source = "*>"*8
#     machine = Machine(source)

#     assert machine.instruction == Instruction.TOGGLE
#     machine.move_right()
#     assert machine.instruction == Instruction.HEAD_RIGHT
#     machine.move_right()
#     assert machine.instruction == Instruction.TOGGLE

#TODO: loop tests