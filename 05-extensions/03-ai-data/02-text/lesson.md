# AI02 — Learn

## Define one searchable representation

Newlines, Unicode composition and accidental indentation can make identical-looking text differ. Normalization should be deterministic and documented. It must not remove meaningful paragraph boundaries or silently pretend it is the original byte sequence.

## Syntax — Python

~~~python
import unicodedata
normalized = unicodedata.normalize("NFC", text)
lines = normalized.replace("\r\n", "\n").replace("\r", "\n").split("\n")
clean_line = lines[0].strip()
~~~
NFC combines canonically equivalent Unicode sequences where defined. split("\n") preserves empty lines; split() would split all whitespace and lose paragraphs. Chunk offsets in AI03 refer to this normalized string, measured in Unicode code points, not raw bytes or model tokens.

Do not lower-case the entire document just to make searching easier. A search index can tokenize/case-normalize separately; preserve readable text for evidence and citations.

[Assignment](exercise.md) · [Hints](help.md)
