#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers
import random

with atheris.instrument_imports(include=['icalevents']):
    from icalevents.icalevents import events

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        events(string_content=fdp.ConsumeRemainingBytes())
    except (TypeError, IndexError, AttributeError):
        if random.random() > 0.999:
            raise
        return -1
    except ValueError as e:
        if 'invalid' or 'content' in str(e):
            return -1
        raise e

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
