#!/bin/sh

# evalmessage: Information on the execution result of the previous run of solution.py by the game server.
# Contestants should consider how to utilize this information themselves.
evalmessage="${1:-""}"

python main.py
