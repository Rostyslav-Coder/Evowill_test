"""Main module"""

import logging
from argparse import ArgumentParser

from bored_api import BoredApi
from database import ActivityDB

# For information on how this module works, I recommend visiting:
# https://docs.python.org/3/library/argparse.html and
# https://docs.python.org/3/library/logging.html

logging.basicConfig(level=logging.INFO)


def main():
    parser = ArgumentParser(description="Get & save random activities from Bored API")
    subparsers = parser.add_subparsers(dest="command")

    new_parser = subparsers.add_parser("new", help="Get new random activity")
    new_parser.add_argument("--type", help="Filter by type of activity")
    new_parser.add_argument(
        "--participants", type=int, help="Filter by number of participants"
    )
    new_parser.add_argument("--price_min", type=float, help="Filter by min price")
    new_parser.add_argument("--price_max", type=float, help="Filter by max price")
    new_parser.add_argument(
        "--accessibility_min", type=float, help="Filter by min accessibility"
    )
    new_parser.add_argument(
        "--accessibility_max", type=float, help="Filter by max accessibility"
    )

    list_parser = subparsers.add_parser("list", help="List of the 5 latest activities")

    args = parser.parse_args()

    api = BoredApi()
    database = ActivityDB()

    if args.command == "new":
        activity = api.get_random_activity(
            type=args.type,
            participants=args.participants,
            price_min=args.price_min,
            price_max=args.price_max,
            accessibility_min=args.accessibility_min,
            accessibility_max=args.accessibility_max,
        )
        database.save_activity(activity=activity)
        logging.info(activity)
        logging.info("New activity saved: %s", {activity["activity"]})
    elif args.command == "list":
        activities = database.get_latest_activities()
        for activity in activities:
            logging.info(activity)


if __name__ == "__main__":
    main()
