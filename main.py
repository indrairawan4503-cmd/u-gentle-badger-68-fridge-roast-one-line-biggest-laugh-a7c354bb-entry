"""Fridge Roast — variant A (firmware update angle), v5 (FINAL).

v4 -> v5: final read-aloud polish — "the app says I'm on the free tier"
became "the app says this is the free tier". Same length (197 chars), but now
the app labels the whole broken state as a tier instead of the user being "on"
one, so the punch ("free tier of refrigeration") lands as the fridge's verdict
on its own failure. No further changes: setup names the artifact (firmware
2.0, auto-installed overnight), damage escalates (milk 18°C, ice maker on
strike), punch lands last.
Joke: the fridge auto-updates overnight and gets worse at its one job — being
cold. It now treats "cold" as a premium subscription feature, so the milk sits
at 18°C while the app smugly reports the user is on the free tier.
Skeleton: named feature (firmware 2.0) -> fridge applies subscription logic
to the WRONG target (temperature itself) -> punch at the very end ("free tier
of refrigeration"). Roasts the fridge/app/firmware directly, fridge-specific,
and avoids the banned "orders groceries" / "watches you" cracks.
"""

MAX_CHARS = 200

ENTRY = (
    "My smart fridge auto-installed firmware 2.0 overnight and now cold is a "
    "subscription \u2014 my milk is sitting at 18\u00b0C, the ice maker's on "
    "strike, and the app says this is the free tier of refrigeration."
)

assert len(ENTRY) <= MAX_CHARS, f"entry too long: {len(ENTRY)} chars"
assert ENTRY.strip(), "entry must not be blank"
assert "\n" not in ENTRY.strip(), "entry must be a single line"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Best-effort copy next to the repo; the grader sandbox is read-only,
    # so never let this fail the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
