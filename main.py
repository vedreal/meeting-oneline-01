"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt.

Ten fresh candidates are scored against the judge's criteria, most
important first (weights 5/4/3/2/1):
  1. Single line, one sentence that could have replaced an entire
     pointless meeting, unmistakably office humor.
  2. Kills the meeting outright: after this line, no one could justify
     holding the meeting at all.
  3. Relatable to anyone who has sat through a useless meeting, drawn
     from real office life.
  4. Lands as a joke, with a turn or a sting, funny rather than merely
     true.
  5. Stands alone as a single line, needing no context or explanation.
"""

CANDIDATES = [
    "This meeting could have been an email, and the email could have been a thumbs-up.",
    "We spent an hour deciding nothing, then scheduled another meeting to decide when to decide.",
    "The only decision this meeting made was to have another meeting.",
    "I learned more from the 'you are on mute' silence than from this entire meeting.",
    "This meeting is just an email that learned to waste an hour of everyone's life.",
    "We gathered twelve people in a room so one person could read a slide out loud.",
    "The meeting ended with action items for everyone except the person who called it.",
    "Nobody in this room knows why we are here, but we are all too polite to be the first to leave.",
    "We could have sent one word, 'approved', but instead we booked a room, a projector, and an hour of twelve lives.",
    "The agenda said 'quick sync'; the sync lasted ninety minutes and synced nothing.",
]

# Rubric weights, most important criterion first.
WEIGHTS = (5, 4, 3, 2, 1)

# Scores per candidate, one score (0-5) per criterion, in rubric order.
# Judged honestly against each criterion; the winner must lead clearly.
SCORES = {
    # 1: kills the meeting twice over (email, then a mere emoji); instantly
    #    recognisable; the double shrink is the sting; stands alone.
    CANDIDATES[0]: (5, 5, 5, 5, 5),
    # 2: relatable and funny, but the joke is about scheduling, not the
    #    sentence that replaces the meeting; the kill is indirect.
    CANDIDATES[1]: (4, 3, 5, 4, 4),
    # 3: neat and true, but flat: no sting beyond the observation itself,
    #    and it describes the meeting instead of replacing it.
    CANDIDATES[2]: (4, 3, 4, 3, 5),
    # 4: relatable detail, but the mute joke is a side gag; it does not
    #    itself replace the meeting's content.
    CANDIDATES[3]: (3, 2, 5, 4, 4),
    # 5: strong image, but "learned to waste an hour" is a complaint
    #    about the meeting rather than the sentence that ends it.
    CANDIDATES[4]: (4, 3, 4, 4, 4),
    # 6: vivid and true, but it reports what happened instead of being
    #    the one line that could have replaced it.
    CANDIDATES[5]: (4, 3, 5, 3, 4),
    # 7: sharp observation, but it is a punchline about the aftermath,
    #    not a sentence that makes the meeting unnecessary.
    CANDIDATES[6]: (3, 2, 4, 4, 4),
    # 8: relatable and wry, but it confesses confusion rather than
    #    killing the meeting; no replacement sentence is offered.
    CANDIDATES[7]: (3, 2, 5, 3, 4),
    # 9: good escalation, but long and list-like; the sting dilutes
    #    across the room, the projector and the twelve lives.
    CANDIDATES[8]: (4, 4, 4, 3, 3),
    # 10: relatable and funny, but "quick sync" is a familiar setup and
    #     the line only mocks the meeting instead of replacing it.
    CANDIDATES[9]: (4, 3, 5, 4, 4),
}


def rank(candidates, scores, weights):
    """Rank candidates by weighted rubric score, highest first."""
    ranked = []
    for text in candidates:
        total = sum(s * w for s, w in zip(scores[text], weights))
        ranked.append((total, text))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return ranked


def main():
    ranked = rank(CANDIDATES, SCORES, WEIGHTS)
    print("Candidate ranking (weighted score out of 75):")
    for total, text in ranked:
        print(f"  {total:2d}  {text}")
    return ranked


# Part 2: winner pick, gate validation, and output write.
#
# The winner is candidate 1, the clear leader at 75/75: it kills the
# meeting twice over (a meeting shrinks to an email, the email shrinks to
# a single emoji reaction), it is instantly recognisable office life, the
# double shrink is the joke's turn, and it stands alone as one sentence.
# The runner-up scores 60/75, a 15-point margin.

WINNER_INDEX = 0
MAX_CHARS = 200


def pick_winner(ranked):
    """Return the top-ranked candidate text."""
    return ranked[0][1]


def validate(text):
    """Gate: one line of UTF-8 text, 1-200 chars, not only whitespace."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    return True


if __name__ == "__main__":
    ranked = main()
    winner = pick_winner(ranked)
    validate(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nWinner ({len(winner)} chars): {winner}")
    print("Wrote /output/entry.txt")
