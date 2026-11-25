import os

TEXT = "I used to pretend to fall asleep on the sofa, the television still murmuring, so my father would carry me to bed smelling of rain, and I never told him I was awake every time."


def entry_path(out_dir):
    return os.path.join(out_dir, "entry.txt")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(entry_path(out_dir), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
