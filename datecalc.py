#!/usr/bin/env python3
"""DateCalc - everyday date arithmetic from the command line.

Subcommands:
    diff      days between two dates
    add       add or subtract days from a date
    age       exact age (years, months, days) from a date of birth
    workdays  count Monday-to-Friday days in a range

Standard library only (datetime, argparse, sys).
"""

import argparse
import sys
from datetime import date, timedelta


def parse_date(value, parser, option):
    """Parse a YYYY-MM-DD date or exit 2 with a clear message."""
    try:
        return date.fromisoformat(value)
    except (ValueError, TypeError):
        parser.error(
            "invalid date for %s: %r (expected YYYY-MM-DD)" % (option, value)
        )


def fmt(d):
    """Format as '2026-11-10 (Tuesday)'."""
    return "%s (%s)" % (d.isoformat(), d.strftime("%A"))


def cmd_diff(args, parser):
    start = parse_date(args.from_date, parser, "--from")
    end = parse_date(args.to_date, parser, "--to")
    days = (end - start).days
    line = "%s to %s: %d days" % (fmt(start), fmt(end), days)
    if days < 0:
        line += " (second date is earlier)"
    print(line)
    weeks, remainder = divmod(abs(days), 7)
    print("That is %d weeks and %d days." % (weeks, remainder))
    return 0


def cmd_add(args, parser):
    start = parse_date(args.date, parser, "--date")
    result = start + timedelta(days=args.days)
    if args.days < 0:
        expr = "%s - %d days" % (fmt(start), abs(args.days))
    else:
        expr = "%s + %d days" % (fmt(start), args.days)
    print("%s = %s" % (expr, fmt(result)))
    return 0


def cmd_age(args, parser):
    dob = parse_date(args.dob, parser, "--dob")
    if args.today:
        today = parse_date(args.today, parser, "--today")
    else:
        today = date.today()
    if dob > today:
        parser.error("date of birth %s is after %s" % (dob.isoformat(), today.isoformat()))

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        # Borrow the length of the month immediately before today's month.
        if today.month == 1:
            prev_month_first = date(today.year - 1, 12, 1)
        else:
            prev_month_first = date(today.year, today.month - 1, 1)
        first_of_this = date(today.year, today.month, 1)
        days_in_prev = (first_of_this - prev_month_first).days
        days += days_in_prev
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    print("Age: %d years, %d months, %d days" % (years, months, days))
    return 0


def cmd_workdays(args, parser):
    start = parse_date(args.from_date, parser, "--from")
    end = parse_date(args.to_date, parser, "--to")
    if start > end:
        print(
            "error: --from date %s is after --to date %s"
            % (start.isoformat(), end.isoformat()),
            file=sys.stderr,
        )
        return 2
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # Monday=0 .. Friday=4
            count += 1
        current += timedelta(days=1)
    print(
        "Working days (Mon-Fri) from %s to %s inclusive: %d"
        % (start.isoformat(), end.isoformat(), count)
    )
    return 0


def build_parser():
    parser = argparse.ArgumentParser(
        prog="datecalc.py",
        description="Everyday date arithmetic: differences, adding days, "
        "ages and working-day counts.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_diff = sub.add_parser("diff", help="days between two dates")
    p_diff.add_argument("--from", dest="from_date", required=True,
                        help="start date, YYYY-MM-DD")
    p_diff.add_argument("--to", dest="to_date", required=True,
                        help="end date, YYYY-MM-DD")
    p_diff.set_defaults(func=cmd_diff)

    p_add = sub.add_parser("add", help="add or subtract days from a date")
    p_add.add_argument("--date", required=True, help="base date, YYYY-MM-DD")
    p_add.add_argument("--days", required=True, type=int,
                       help="days to add (may be negative)")
    p_add.set_defaults(func=cmd_add)

    p_age = sub.add_parser("age", help="exact age from a date of birth")
    p_age.add_argument("--dob", required=True, help="date of birth, YYYY-MM-DD")
    p_age.add_argument("--today", default=None,
                       help="reference date, YYYY-MM-DD (default: today)")
    p_age.set_defaults(func=cmd_age)

    p_work = sub.add_parser("workdays", help="count Mon-Fri days in a range")
    p_work.add_argument("--from", dest="from_date", required=True,
                        help="start date, YYYY-MM-DD")
    p_work.add_argument("--to", dest="to_date", required=True,
                        help="end date, YYYY-MM-DD")
    p_work.set_defaults(func=cmd_workdays)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args, parser)


if __name__ == "__main__":
    sys.exit(main())
