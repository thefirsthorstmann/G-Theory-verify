"""An abstract's statement, without its closing note on the public suite and Lean 4.

CC, 28 October 2026, during the upload to Zenodo: "many of these new versions do not have the git or the lean 4 notes in
the abstracts, can you check and update before I continue?" Every record's abstract now closes on the public suite's
address and, where the record formalizes its arithmetic, on the Lean 4 note. That closing note is the record's apparatus,
not its statement: the 150-250 words of the papers (CLAUDE.md section 11, rule 4) are counted on what comes before it.

The note is the run of closing sentences each of which names the suite's address or Lean 4; a sentence naming neither
ends the run, so nothing of the statement is ever stripped.
"""
import re

ADDRESS = "github.com/thefirsthorstmann/g-theory-verify"


def statement_of(abstract):
    """The abstract up to its closing note."""
    sentences = re.split(r"(?<=[.!?])\s+", abstract.strip())
    while sentences and (ADDRESS in sentences[-1] or "Lean 4" in sentences[-1]):
        sentences.pop()
    return " ".join(sentences)


def note_of(abstract):
    """The closing note itself (empty when the abstract has none)."""
    return abstract.strip()[len(statement_of(abstract)):].strip()


def words(text):
    """Words as the batteries count them: a bare minus sign is not a word."""
    return [w for w in text.split() if re.search(r"\w", w)]
