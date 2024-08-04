#!/usr/bin/env python3

from chunk import Chunks
from lines import nonempty
import ollama
import progressbar

TEMPLATE = """Fix style and summarize this text to one paragraph. Write ONLY fixed text without introduction and conclusion.

```
{text}
```"""

WIDGETS = [
    ' [',
    progressbar.Timer(),
    '] ',
    progressbar.Bar(),
    ' (',
    progressbar.ETA(),
    ') ',
]


def convert(path, output, factor, model, progress):
    with open(path, "r") as f:
        chunks = list(Chunks(nonempty(f), factor))

        if progress:
            chunks = progressbar.progressbar(chunks, widgets=WIDGETS)

        for chunk in chunks:
            text = "\n\n".join((line.rstrip() for line in chunk))
            content = TEMPLATE.format(text=text)
            message = {"role": "user", "content": content}
            response = ollama.chat(model=model, messages=[message])

            output.write(response["message"]["content"].strip())
            output.write("\n\n")
            output.flush()
