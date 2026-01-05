from gib_lang.runner import Machine, Tape, run

def test_run_toggle() -> None:
    source = "FAFAFAFA" * 8
    tape_size = 8

    machine, tape = run(
        source,
        tape_size,
    )

    assert machine == source
    assert tape == "11111111"

    source = "FAFAFAFAFUFUFAFAFAFAFUFUFUFUFAFAFAFAFUFU" * 8 
    machine, tape = run(
        source,
        tape,
        1000,
    )

    assert machine == source
    assert tape == "00000000"


def test_run_callback() -> None:
    source = "FAFAFAFA" * 8
    tape_size = 8

    def callback(machine: Machine, tape: Tape) -> bool:
        return machine.steps == 5

    machine, tape = run(
        source,
        tape_size,
        callback=callback,
    )

    assert machine.steps == 5
    assert tape == "11111000"


def test_run_max_steps() -> None:
    source = "FAFAFAFA" * 8
    tape_size = 8

    machine, tape = run(
        source,
        tape_size,
        max_steps=4,
    )

    assert machine.steps == 4
    assert tape == "11110000"


def test_run_loop_behavior() -> None:
    source = "FUFUFAFAFAFAFUFU"
    machine, tape = run(source, 8, max_steps=10)
    
    assert machine.steps == 1
    assert tape == "00000000"

    source = "FAFAFAFAFUFUFAFAFUFUFAFAFAFAFUFUFUFUFAFAFAFAFUFUFAFAFUFU"*8
    machine, tape = run(source, 8, max_steps=10)
    assert machine.steps == 10