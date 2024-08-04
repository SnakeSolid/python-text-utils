#!/usr/bin/env python3


def nonempty(source):
    return [line for line in (line.strip() for line in source) if line]
