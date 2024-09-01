# hwmcc24_submission

Our submission for HWMCC24

## How to run?

First add `./executables` to `PATH`:
```commandline
export PATH=executables/:$PATH
```

Then the most direct way to run our submission is with the following command:
```commandline
python3 ./scripts/pavy.py <models>
```
This command will write the proof in `./certificate.aig` or
`./certificate.aag` and the counterexample in `./cex`.

To add more parameters such as timeout, memory limit, and to change location of witnesses you can
add arguments as described in:
```commandline
python3 ./scripts/pavy.py --help
```

# Submitters

* Dr. Yakir Vizel
* Basel Khouri
* Andrew Luka