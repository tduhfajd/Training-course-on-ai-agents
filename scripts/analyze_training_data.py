#!/usr/bin/env python3
"""Reproduce the synthetic course example; no network, dependencies or writes."""
import argparse
import csv
import json
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["event_id", "date", "kind", "cash_rub", "goods_cost_rub", "delivery_cost_rub"]


def amount(value, field, event_id):
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError(f"{event_id}: invalid {field}") from exc
    if not result.is_finite():
        raise ValueError(f"{event_id}: non-finite {field}")
    return result


def analyze(path):
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError("Unexpected columns; use the course schema")
        rows = list(reader)
    if not rows:
        raise ValueError("No events; an empty input is not a successful report")
    events = {}
    duplicates = 0
    for row in rows:
        if None in row or any(value is None for value in row.values()):
            raise ValueError("Malformed CSV row")
        event_id = row["event_id"]
        if not event_id:
            raise ValueError("Missing event_id")
        date.fromisoformat(row["date"])
        if event_id in events:
            if events[event_id] != row:
                raise ValueError(f"{event_id}: conflicting rows; do not deduplicate silently")
            duplicates += 1
        else:
            events[event_id] = row
    cash = Decimal(0)
    goods = Decimal(0)
    delivery = Decimal(0)
    unknown = []
    for event_id, row in events.items():
        value = amount(row["cash_rub"], "cash_rub", event_id)
        cost = amount(row["goods_cost_rub"], "goods_cost_rub", event_id)
        if row["kind"] not in ("sale", "refund"):
            raise ValueError(f"{event_id}: unknown kind")
        if (row["kind"] == "sale" and value <= 0) or (row["kind"] == "refund" and value >= 0):
            raise ValueError(f"{event_id}: unexpected cash sign")
        if cost < 0:
            raise ValueError(f"{event_id}: negative goods expense")
        cash += value
        goods += cost
        if row["delivery_cost_rub"] == "":
            unknown.append(event_id)
        else:
            fee = amount(row["delivery_cost_rub"], "delivery_cost_rub", event_id)
            if fee < 0:
                raise ValueError(f"{event_id}: negative delivery expense")
            delivery += fee
    residual = cash - goods - delivery
    return {
        "synthetic_data": True,
        "input_rows": len(rows),
        "unique_events": len(events),
        "exact_duplicates": duplicates,
        "period": [min(row["date"] for row in events.values()),
                   max(row["date"] for row in events.values())],
        "cash_total_rub": str(cash),
        "goods_expenses_known_rub": str(goods),
        "delivery_expenses_known_rub": str(delivery),
        "residual_before_unknown_and_unlisted_expenses_rub": str(residual),
        "unknown_delivery_event_ids": unknown,
        "complete_residual_for_listed_expenses_rub": None if unknown else str(residual),
        "full_profit_rub": None,
        "limitation": "Unlisted expenses are not modeled; this is not full profit.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", nargs="?", type=Path, default=ROOT / "examples/data/operations.csv")
    args = parser.parse_args()
    try:
        result = analyze(args.csv_path)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Data check failed: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
