def check_duplicate_ids(file_path):
    ids = {}
    duplicates = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if "=" in line:
                key = line.split("=", 1)[0].strip()

                if key in ids:
                    # Store the first occurrence and any duplicates
                    if key not in duplicates:
                        duplicates[key] = [ids[key]]
                    duplicates[key].append(line_number)
                else:
                    ids[key] = line_number

    if not duplicates:
        print("✔ No duplicate Key IDs found.")
    else:
        print("❌ Duplicate Key IDs detected:")
        for key, lines in duplicates.items():
            print(f"- {key} appears on lines: {', '.join(map(str, lines))}")


# Example usage:
check_duplicate_ids("ar_DZ.lang")