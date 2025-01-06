import os
import logging

# from a2g.a2g import a2g
from a2g.tasksolving import TaskSolving

# from a2g.gui import GUI
from a2g.logging import logger
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "--task",
    type=str,
    default="tasksolving/brainstorming",
)
parser.add_argument("--debug", action="store_true")
parser.add_argument(
    "--tasks_dir",
    type=str,
    default=os.path.join(os.path.dirname(__file__), "..", "a2g", "tasks"),
)
args = parser.parse_args()

logger.set_level(logging.DEBUG if args.debug else logging.INFO)


def cli_main():
    a2gpipeline = TaskSolving.from_task(args.task, args.tasks_dir)
    a2gpipeline.run()


if __name__ == "__main__":
    cli_main()
