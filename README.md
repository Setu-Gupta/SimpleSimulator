# SimpleSimulator
A Simple simulator for a custom ISA

## Dependencies
The trace graph generator depends on `matplotlib`.

## How to run
Execute the `run` file. Pass the binary via `stdin`. The output is written to `stdout`:

```sh
$ ./run < path/to/binary > path/to/dump
```

## How to view the memory access pattern
The generated pattern is stored as a `.png` file in the root directory.
