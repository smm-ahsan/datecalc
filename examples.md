# Examples

Real output from DateCalc, captured from actual runs.

## Days between two dates

Command:

```bash
python3 datecalc.py diff --from 2026-11-10 --to 2026-12-25
```

Output:

```
2026-11-10 (Tuesday) to 2026-12-25 (Friday): 45 days
That is 6 weeks and 3 days.
```

## Add days to a date

Command:

```bash
python3 datecalc.py add --date 2026-11-10 --days 30
```

Output:

```
2026-11-10 (Tuesday) + 30 days = 2026-12-10 (Thursday)
```

## Exact age

Command:

```bash
python3 datecalc.py age --dob 1996-03-23 --today 2026-11-10
```

Output:

```
Age: 30 years, 7 months, 18 days
```

## Working days in a week

Command:

```bash
python3 datecalc.py workdays --from 2026-11-09 --to 2026-11-15
```

Output:

```
Working days (Mon-Fri) from 2026-11-09 to 2026-11-15 inclusive: 5
```
