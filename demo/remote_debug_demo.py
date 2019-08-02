"""
debug_demo.py
Remote Debug Demo Runner

Enables easy Windide remote debug of demo controller/agents

This gets around the relative imports in runners.faber runners.alice
And terminal issues with the asyncio server


"""


import os
import sys
import argparse

#  append parent directory to path to find demo package
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from  demo.faberfix import main



parser = argparse.ArgumentParser(description='Run a Demo Agent: faber or alice.')

p.add_argument('-a', '--agent',
        action='store',
        default='faber',
        help="Name of demo agent: faber or alice.")


def main(args=None):
    import runners
    args = parser.parse_args(args=args)
    print(args.names)
    agent = args.agent


if __name__ == "__main__":
    main()

