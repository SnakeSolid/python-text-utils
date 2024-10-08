#!/usr/bin/env python3

from textutils.lines import nonempty


def convert(path, output, min_lines, max_lines):
    with open(path, "r", encoding="utf-8") as f:
        paragraph = []
        line_length = 0

        for line in nonempty(f):
            if len(paragraph) < min_lines:
                paragraph.append(line.rstrip())
                line_length += len(line)
            elif len(paragraph) < max_lines:
                average_len = int(line_length / len(paragraph))

                if len(line) < average_len:
                    output.write(" ".join(paragraph))
                    output.write("\n\n")

                    paragraph = []
                    line_length = 0
                else:
                    paragraph.append(line.rstrip())
                    line_length += len(line)
            else:
                output.write(" ".join(paragraph))
                output.write("\n\n")

                paragraph = []
                line_length = 0

        if len(paragraph) > 0:
            output.write(" ".join(paragraph))
            output.write("\n\n")
