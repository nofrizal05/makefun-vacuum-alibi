# The Vacuum's Alibi — one-line excuse for a missed spot.
# Joke setup: the vacuum's lidar mistakes a sock pile for a sleeping animal,
# so it leaves the dust as a blanket under a strict no-vacuuming-wildlife policy.
import os

ENTRY = (
    "I skipped that corner on purpose: my lidar classified the sock pile "
    "as a sleeping animal, and company policy forbids vacuuming wildlife."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
