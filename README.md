# hwmcc24_submission

Our submission for HWMCC24

# Pavy Script

## How to Run the Script

To execute the script, use the following command:

```bash
python3 ./scripts/pavy.py <model>

```

The script will launch multiple engines, each with a different configuration. Before completing, it will display the following information: the "Winner" engine, the result status (`SAFE`, `UNSAFE`, or `UNDETERMINED`), and the location of the "Witness" file.

The engine that first determines the safety of the provided model will be declared the "Winner." If no engine successfully completes the task, the winner will be listed as "Unknown."

## Example Run

```bash
python3 scripts/pavy.py hwmcc17/6s109.aig

```
```output
[pavy] starting run with fname=hwmcc17/6s109.aig
[pavy] running: [3718617, 3718618, 3718619, 3718620, 3718621, 3718622, 3718623, 3718624, 3718625, 3718626, 3718629, 3718630, 3718635]
Winner:  abcpdr
Result:  SAFE
Witness: certificate.aig
```

## Certificate Information

If the model is determined to be `SAFE`, a certificate will be generated in the current working directory. Depending on the engine used, the certificate may be in binary or non-binary format, resulting in a file named either `certificate.aig` or `certificate.aag`. The correct file name will be indicated by the `Witness` path in the output.

If the model is found to be `UNSAFE`, a counterexample (cex) will be saved as `cex` in the current working directory.

You can specify a custom name for the certificate or counterexample by using the `--certificate <desired name>` or `--cex <desired name>` options. The script will automatically append the appropriate extension (aag or aig) to the provided name.

# Submitters

* Dr. Yakir Vizel
* Basel Khouri
* Andrew Luka