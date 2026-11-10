# DateCalc

Everyday date arithmetic from the command line: date differences, adding days, exact ages and working-day counts.

## Subcommands

- `diff` — days between two dates, with weekday names and a weeks-and-days breakdown
- `add` — add or subtract days from a date
- `age` — exact age (years, months, days) from a date of birth
- `workdays` — count Monday-to-Friday days in a date range, inclusive

## Requirements

- Python 3
- Standard library only (`datetime`) — nothing to install

## Usage

```bash
# Days between two dates
python3 datecalc.py diff --from 2026-11-10 --to 2026-12-25

# Add 30 days to a date (use a negative number to subtract)
python3 datecalc.py add --date 2026-11-10 --days 30

# Exact age on a given date (--today is optional and defaults to today)
python3 datecalc.py age --dob 1996-03-23 --today 2026-11-10

# Working days (Mon-Fri) in a range, inclusive
python3 datecalc.py workdays --from 2026-11-09 --to 2026-11-15
```

All dates use the `YYYY-MM-DD` format. A malformed date exits with code 2 and a clear error message, never a traceback.

See [examples.md](examples.md) for real captured output.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Muhammad Ahsan Anwar.
