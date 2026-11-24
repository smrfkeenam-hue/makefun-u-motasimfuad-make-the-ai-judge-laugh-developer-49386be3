import os

ENTRY = "The outage was caused by a cron job I wrote in 2021 — it finally ran today and did exactly what I told it to do."


def output_path():
    return os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )


def write_entry(text, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY, output_path())


if __name__ == "__main__":
    main()
