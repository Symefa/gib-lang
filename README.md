# gib-lang

<img width="300" height="300" alt="gib-lang" src="https://github.com/user-attachments/assets/417e1208-173f-46ad-be60-e19ad080582a" />

**Gibberish** a minimalist, dynamic, and turing-complete programming language, it is based on [Reversible BitFuck](https://esolangs.org/wiki/Reversible_Bitfuck). to further reduce it with only 3 instruction.

## The Instruction

- `FAFAFAFA` Toggle and Move Head Forward, in RBF `+>`
- `FUFUFAFA` Move Head Backward and Open Loop, in RBF `<(`
- `FAFAFUFU` Closes Loop, in RBF `)`

you can run command using

```sh
gib run -t 3 "FAFAFAFA FUFUFAFA FAFAFUFU #toggle head"
```

Here the example instruction combination

```sh
FAFAFAFA FUFUFAFA FAFAFUFU  #toggle head
FAFAFAFA FUFUFAFA FAFAFUFU FAFAFAFA #move forward
FUFUFAFA FAFAFUFU #move backward
FAFAFAFA FUFUFAFA FAFAFUFU FAFAFAFA FUFUFAFA #open loop
FAFAFUFU #close loop
```

## How It Works

The program simulate turing machine with moving head and 1-bit tape

![Presentation1](https://github.com/user-attachments/assets/e00d3278-40a5-4ef2-90df-d9ea3eb752d6)

## How to Install

Giberish can be installed from pypi

```sh
pip install gib-lang
```
