import enum

class Instruction(enum.Enum):
    """
    Gibberish Language Syntax
    -------------------------
    FAFA : if the current command counter is 0, toggle current tape head bit then move the tape head right, toggle the command counter
    FUFU : 1. if the current command counter is 0 and current tape head bit is 0, move the machine head right until found matching FUFU
           2. if the current comand counter is 1, move the tape head left, toggle it, then move the tape head left,
              if the current tape head bit is 0, move the machine head left until found matching FUFU
           3. if the machine head is not moved in step 1 or 2, toggle the command counter

    based on https://esolangs.org/wiki/Talk:Picofuck#Candidate_languages
    """

    TOGGLE_HEAD_RIGHT = "FAFAFAFA"  # *
    HEAD_LEFT_LOOP_START = "FUFUFAFA"  # {
    LOOP_END = "FAFAFUFU"  # }
    NO_OP = "FUFUFUFU"
