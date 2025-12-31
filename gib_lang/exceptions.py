class GibError(Exception):
    pass


class MachineHeadError(GibError):
    """Raise Error when Head out of bounds"""


class InvalidInstructionError(GibError):
    """Raise Error when instruction is invalid"""
