from gib_lang.runner import Machine, Tape, run

# def test_run_toggle() -> None:
#     source = "*>" * 8
#     tape_size = 8

#     machine, tape = run(
#         source,
#         tape_size,
#     )

#     assert machine == source
#     assert tape == "11111111"

#     source = "*<" * 8
#     machine, tape = run(
#         source,
#         tape,
#     )

#     assert machine == source
#     assert tape == "00000000"


# def test_run_callback() -> None:
#     source = "*>" * 8
#     tape_size = 8

#     def callback(machine: Machine, tape: Tape) -> bool:
#         return machine.steps == 5

#     machine, tape = run(
#         source,
#         tape_size,
#         callback=callback,
#     )

#     assert machine.steps == 5
#     assert tape == "11100000"


# def test_run_max_steps() -> None:
#     source = "*>" * 8
#     tape_size = 8

#     machine, tape = run(
#         source,
#         tape_size,
#         max_steps=5,
#     )

#     assert machine.steps == 5
#     assert tape == "11100000"


# def test_run_loop_behavior() -> None:
#     source = "()"
#     machine, tape = run(source, 8, max_steps=10)
    
#     assert machine.steps == 1
#     assert tape == "00000000"

#     source = "*(>)"
#     machine, tape = run(source, 8, max_steps=10)
#     assert machine.steps == 10