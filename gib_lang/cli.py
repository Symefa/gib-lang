import argparse
import logging
import os
import sys

from . import Machine, Tape, run, __version__

pr_ascii = False

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.add_argument(
        "--log-level",
        help="The log level, default is INFO",
        default="INFO",
    )

    subparsers = parser.add_subparsers(
        required=True,
        dest="subcommand",
    )

    run_parser = subparsers.add_parser("run", help="Run a code")

    run_parser.add_argument("source", help="The code to run")
    run_parser.add_argument(
        "-t",
        "--tape",
        help="The initial tape to use. Can be an integer to use as the tape size, or a string of 1s and 0s",
        default="8",
    )
    run_parser.add_argument(
        "--max-steps",
        type=int,
        help="The maximum number of steps",
        default=10000,
    )

    run_parser.add_argument(
        "-c",
        "--ascii",
        action=argparse.BooleanOptionalAction
    )

    args = parser.parse_args()

    logger = logging.getLogger("gib")

    logger.setLevel(args.log_level.upper())
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)05s %(name)s: %(message)s"))
    logger.addHandler(handler)

    if args.subcommand == "run":
        run_main(args, logger)
    else:
        raise ValueError(f"Unknown command: {args.subcommand}")


def pipe_print(*args: object, **kwargs: object) -> None:
    try:
        print(*args, **kwargs)  # type: ignore
        sys.stdout.flush()
    except BrokenPipeError:
        # Gracefully handle broken pipe when e.g. piping to head
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)

def _preprocess(source: str) -> str:
    source = source.replace("\\n", "\n")
    raws = source.split("\n")
    raws = [raw.split("#", 1)[0] for raw in raws]
    source = "".join(raws)
    source = source.replace(" ", "")
    return source

def process_file(path: str) -> str:
    try:
        with open(path, 'r') as f:
            content = f.read()
            return _preprocess(content)
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return ""

def run_main(args: argparse.Namespace, logger: logging.Logger) -> None:
    # Check if tape is a string containing only 1s and 0s
    if all(x in "01" for x in args.tape):
        logger.debug("Using --tape as a string")
        tape = args.tape
    else:
        logger.debug("Using --tape as an integer")
        tape = int(args.tape)

    def callback(machine: Machine, tape: Tape) -> bool:
        logger.debug(
            f" {machine.steps} {machine.instruction.value} {machine.head:02d} | {tape.head:02d} {tape}"
        )
        return False
    source = ""
    if args.source.find('/') != -1:
        source = process_file(args.source)
    else:
        source = args.source

    _machine, tape = run(
        _preprocess(source),
        tape,
        max_steps=args.max_steps,
        callback=callback,
    )

    if args.ascii:
        pipe_print(tape.to_ascii())
    else:
        pipe_print(tape)


if __name__ == "__main__":
    main()
