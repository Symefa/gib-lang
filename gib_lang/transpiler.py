import logging
from collections.abc import Sequence
from itertools import islice

from .instruction import Instruction, Syntax

logger = logging.getLogger("gib")

__SYNTAX_TRANSLATION = {
    "FAFAFAFA": [
        Instruction.TOGGLE,
        Instruction.HEAD_RIGHT,
    ],
    "FUFUFAFA": [
        Instruction.HEAD_LEFT,
        Instruction.LOOP_START,
    ],
    "FAFAFUFU": [Instruction.LOOP_END],
    "FUFUFUFU": [],
}

_INSTRUCTIONS_TRANSLATION = {
    "*>": Syntax.TOGGLE_HEAD_RIGHT,
    "<(": Syntax.HEAD_LEFT_LOOP_START,
    ")": Syntax.LOOP_END,
}


def batched(iterable, n):
    if n < 1:
        raise ValueError("n must be at least one")
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch


def transpile(source: str) -> str:
    """Transpile source code from Gibberish to RBF"""
    source = _preprocess(source)
    if "FUFU" in source or "FAFA" in source:
        # Gibberish to RBF
        source = _preprocess(source)
        result = ""
        for batch in batched(source, 8):
            batch_str = "".join(batch)
            if batch_str in __SYNTAX_TRANSLATION:
                instructions = __SYNTAX_TRANSLATION[batch_str]
                replacement = "".join(instruction.value for instruction in instructions)
                result += replacement
                logger.debug(f"Replaced {batch_str} with {replacement}")
        if "FUFU" in result or "FAFA" in result:
            logger.debug(f"Remaining syntax to replace: {result}")
            raise ValueError("transpilation resulted in incomplete RBF syntax")
        return result
    # TODO: RBF to Gibberish
    else:
        raise ValueError("source does not contain valid Gibberish syntax")


def _preprocess(source: str) -> str:
    source = source.replace("\\n", "\n")
    raws = source.split("\n")
    raws = [raw.split("#", 1)[0] for raw in raws]
    source = "".join(raws)
    source = source.replace(" ", "")
    return source
