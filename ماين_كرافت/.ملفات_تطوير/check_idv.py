import re

def check_multiple_pairs(file_path):
    # Pattern matches: identifier=value
    pattern = re.compile(r"\b[^=\s]+=")

    with open(file_path, "r", encoding="utf-8") as f:
        line_number = 1
        for line in f:
            original = line.rstrip("\n")

            # Find all KEY= matches
            matches = pattern.findall(line)

            if len(matches) > 1:
                print(f"[Error] Line {line_number} contains multiple identifiers:")
                print(f"  {original}")

            line_number += 1


# Example:
check_multiple_pairs("ar_DZ.lang")
