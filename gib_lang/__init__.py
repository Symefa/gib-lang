"""
Gibberish Language (gib-lang) interpreter
===============================================
3 Instructions, Reversible Turing Tarpit, Esoteric Programming Language
based on https://esolangs.org/wiki/Talk:Picofuck#Candidate_languages
"""

__version__ = "0.1.0"
__author__ = "Alifa Izzan Akhsani"
__license__ = "MIT"

from . import machine, tape, runner, transpiler

Machine = machine.Machine
Tape = tape.Tape
run = runner.run
transpile = transpiler.transpile

__all__ = ["Machine", "Tape", "run", "transpile"]
