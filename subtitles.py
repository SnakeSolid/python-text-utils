#!/usr/bin/env python3

import json


def convert(path, output):
    with open(path, "r") as f:
        data = json.load(f)

        for event in data["events"]:
            if "segs" in event:
                for line in ("".join((seg["utf8"] for seg in event["segs"]))):
                    output.write(line)
