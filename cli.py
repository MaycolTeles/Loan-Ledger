#!/usr/bin/env python3
import click
import sqlite3

import os
import csv
from datetime import datetime, timedelta
from typing import Dict

from src import EventHandler


@click.group()
@click.option("--debug/--no-debug", default=False, help="Debug output, or no debug output.")
@click.pass_context
def interface(ctx: Dict, debug: bool) -> None:
    """Ampla engineering takehome ledger calculator."""
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug  # you can use ctx.obj['DEBUG'] in other commands to log or print if DEBUG is on
    ctx.obj["DB_PATH"] = os.path.join(os.getcwd(), "db.sqlite3")
    if debug:
        click.echo(f"[Debug mode is on]")


@interface.command()
@click.pass_context
def create_db(ctx: Dict) -> None:
    """Initialize sqlite3 database."""
    if os.path.exists(ctx.obj["DB_PATH"]):
        click.echo("Database already exists")
        return

    with sqlite3.connect(ctx.obj["DB_PATH"]) as connection:
        if not connection:
            click.echo(
                "Error: Unable to create sqlite3 db file. Please ensure sqlite3 is installed on your system and "
                "available in PATH!"
            )
            return

        cursor = connection.cursor()
        cursor.execute(
            """
            create table events
            (
                id integer not null primary key autoincrement,
                type varchar(32) not null,
                amount decimal not null,
                date_created date not null
                CHECK (type IN ("advance", "payment"))
            );
        """
        )
        connection.commit()
    click.echo(f"Initialized database at {ctx.obj['DB_PATH']}")


@interface.command()
@click.pass_context
def drop_db(ctx: Dict) -> None:
    """Delete sqlite3 database."""
    if not os.path.exists(ctx.obj["DB_PATH"]):
        click.echo(f"SQLite database does not exist at {ctx.obj['DB_PATH']}")
    else:
        os.unlink(ctx.obj["DB_PATH"])
        click.echo(f"Deleted SQLite database at {ctx.obj['DB_PATH']}")


@interface.command()
@click.argument("filename", type=click.Path(exists=True, writable=False, readable=True))
@click.pass_context
def load(ctx: Dict, filename: str) -> None:
    """Load events with data from csv file."""
    if not os.path.exists(ctx.obj["DB_PATH"]):
        click.echo(f"Database does not exist at {ctx.obj['DB_PATH']}, please create it using `create-db` command")
        return

    loaded = 0
    with open(filename) as infile, sqlite3.connect(ctx.obj["DB_PATH"]) as connection:
        cursor = connection.cursor()
        reader = csv.reader(infile)
        for row in reader:
            cursor.execute(
                f"insert into events (type, amount, date_created) values (?, ?, ?)", (row[0], row[2], row[1])
            )
            loaded += 1
        connection.commit()

    click.echo(f"Loaded {loaded} events from {filename}")


@interface.command()
@click.argument("end_date", required=False, type=click.STRING)
@click.pass_context
def balances(ctx: Dict, end_date: str = None) -> None:
    """Display balance statistics as of `end_date`."""
    if end_date is None:
        end_date = datetime.now().date()

    else:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    end_date += timedelta(days=1)

    # query events from database example
    with sqlite3.connect(ctx.obj["DB_PATH"]) as connection:
        cursor = connection.cursor()
        result = cursor.execute("select * from events order by date_created asc;")
        events = result.fetchall()

    handle_events = EventHandler(events, end_date)
    balance_entity = handle_events.handle_all_events()

    click.echo("Advances:")
    click.echo("----------------------------------------------------------")
    click.echo(f"{'Identifier':>10}{'Date':>11}{'Initial Amt':>17}{'Current Balance':>20}")

    for advance in balance_entity.advances:
        click.echo(f"{advance.id:>10}{datetime.strftime(advance.event_date, '%Y-%m-%d'):>11}{advance.initial_amount:>17.2f}{advance.current_balance:>20.2f}")

    overall_advance_balance = balance_entity.advance_balance
    overall_interest_payable_balance = balance_entity.interest_payable_balance
    overall_interest_paid = balance_entity.interest_paid
    overall_payments_for_future = balance_entity.payments_for_future

    click.echo("\nSummary Statistics:")
    click.echo("----------------------------------------------------------")
    click.echo(f"Aggregate Advance Balance: {overall_advance_balance:31.2f}")
    click.echo(f"Interest Payable Balance: {overall_interest_payable_balance:32.2f}")
    click.echo(f"Total Interest Paid: {overall_interest_paid:37.2f}")
    click.echo(f"Balance Applicable to Future Advances: {overall_payments_for_future:>19.2f}")


if __name__ == "__main__":
    interface()
