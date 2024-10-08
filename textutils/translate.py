#!/usr/bin/env python3

from textutils.lines import nonempty
from ollama import Client
import progressbar

TEMPLATE = """Translate this text into {language}. Write ONLY translated text without introduction and conclusion.

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


def convert(uri, path, output, model, language, progress):
    with open(path, "r", encoding="utf-8") as f:
        client = Client(uri)
        lines = nonempty(f)

        if progress:
            lines = progressbar.progressbar(lines, widgets=WIDGETS)

        for line in lines:
            content = TEMPLATE.format(language=language, text=line.rstrip())
            message = {"role": "user", "content": content}
            response = client.chat(model=model, messages=[message])

            output.write(response["message"]["content"].strip())
            output.write("\n\n")
            output.flush()
