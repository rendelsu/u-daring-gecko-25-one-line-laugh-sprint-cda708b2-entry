import os

# One original line, everyday life, twist at the end; gate is 1-200 chars.
LINE = "My screen-time report reads like a breakup letter from someone who still lives with me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
