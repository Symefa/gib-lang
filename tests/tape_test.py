import pytest
from gib_lang import Tape

@pytest.fixture
def tape()-> Tape:
    return Tape(8)

def test_tape(tape: Tape) -> None:
    assert len(tape) == 8
    assert tape.head == 0
    assert tape.tape == [False]*8

def test_getitem(tape: Tape) -> None:
    assert tape[0] == False
    assert tape[1:4] == [False, False, False]

def test_copy(tape: Tape) -> None:
    tape2 = tape.copy()
    assert tape == tape2
    assert tape is not tape2

    tape3 = Tape(tape)
    assert tape == tape3
    assert tape is not tape3

def test_hashable(tape: Tape) -> None:
    tape2= tape.copy()
    assert hash(tape) == hash(tape2)
    assert hash(tape) == hash("00000000")

def test_init() -> None:
    tape1 = Tape(5)
    assert tape1.tape == [False, False, False, False, False]

    tape2 = Tape("10101")
    assert tape2.tape == [True, False, True, False, True]

    tape3 = Tape([1, 0, 1, 0])
    assert tape3.tape == [True, False, True, False]

def test_toggle(tape: Tape) -> None:
    assert tape.get == False
    tape._tape[tape.head] = not tape.get
    assert tape.get == True
    tape.toggle()
    assert tape.get == False

def test_reset(tape: Tape) -> None:
    tape.move_right(3)
    tape.toggle()
    assert tape.head == 3
    assert tape.get == True
    tape.reset()
    assert tape.head == 0
    assert tape.tape == [False]*8

def test_head(tape: Tape) -> None:
    assert tape.head == 0

    for i in range(7):
        assert tape.head == i
        tape.move_right()
    assert tape.head == 7
    tape.move_right()
    assert tape.head == 0
    tape.move_left()
    assert tape.head == 7
    for i in range(7, 0, -1):
        assert tape.head == i
        tape.move_left()