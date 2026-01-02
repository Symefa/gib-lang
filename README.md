# gib-lang

[![main](https://github.com/symefa/gib-lang/actions/workflows/publish.yml/badge.svg)](https://github.com/symefa/gib-lang/actions/workflows/publish.yml)
[![PyPI](https://d25lcipzij17d.cloudfront.net/badge.svg?c=eyJhbGciOiJub25lIn0.eyJiIjp7IngiOmZhbHNlLCJ0IjoidjZlIiwibCI6InB5cGkgcGFja2FnZSIsInIiOiIwLjIuMSJ9fQ)](https://pypi.org/project/gib-lang/)

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

or using file

```sh
gib run -c -t 88 ./examples/hidup.gb
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

![turing](https://github.com/user-attachments/assets/00547bbc-1fd1-44b3-9c0f-6ad997640d0b)


## How to Install

Giberish can be installed from pypi

```sh
pip install gib-lang
```
