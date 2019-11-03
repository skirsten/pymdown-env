from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

import re
import os

class EnvPreprocessor(Preprocessor):
    """Handle env in Markdown content."""

    RE_ENV = re.compile(r"\~\~\~\${([a-zA-Z_][a-zA-Z0-9_]*)}\~\~\~")

    def run(self, lines):
        """Process env."""

        new_lines = []
        for line in lines:
            new_lines.append(self.RE_ENV.sub(lambda m: os.getenv(m.group(1), ""), line))

        return new_lines


class EnvExtension(Extension):
    """EnvExtension extension."""

    def extendMarkdown(self, md):
        """Register the extension."""
        md.registerExtension(self)

        # Register instance of "EnvPreprocessor" with a priority of 32 (same as snippet)
        md.preprocessors.register(EnvPreprocessor(md), "envpreprocessor", 32)

def makeExtension(*args, **kwargs):
    """Return extension."""

    return EnvExtension(*args, **kwargs)


