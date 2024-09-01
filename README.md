# hwmcc24_submission

Our submission for HWMCC24

## How to run?

The easiest way to run our submission is with the following command:
```commandline
python3 ./scripts/pavy.py <models>
```
This command will write the prrof in `./certificate.aig` and the counterexample in `./cex`


Examples:
```commandline
python3 ./scripts/pavy.py --cex cex --cert certificate /tmp/model.aig --check --cpu 60 --exit-on-error
```