#!/usr/bin/env python3


class Chunks:

    def __init__(self, iterable, size):
        self.iterable = iter(iterable)
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        chunk = []

        for item in self.iterable:
            chunk.append(item)

            if len(chunk) == self.size:
                return chunk

        if len(chunk) > 0:
            return chunk

        raise StopIteration
