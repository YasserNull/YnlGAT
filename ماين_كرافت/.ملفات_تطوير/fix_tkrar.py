def remove_duplicate_ids(input_file, output_file="cleaned.lang"):
    seen = set()
    cleaned_lines = []
    duplicates = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            stripped = line.strip()

            if "=" in stripped:
                key = stripped.split("=", 1)[0].strip()

                if key in seen:
                    # store duplicates for reporting
                    duplicates.setdefault(key, []).append(line_number)
                    continue  # skip duplicate line
                else:
                    seen.add(key)

            cleaned_lines.append(line)

    # Write cleaned file
    with open(output_file, 'w', encoding='utf-8') as out:
        out.writelines(cleaned_lines)

    # Reporting
    if not duplicates:
        print("✔ No duplicate Key IDs found.")
    else:
        print("❌ Duplicate Key IDs were removed:")
        for key, lines in duplicates.items():
            print(f"- {key} removed from lines: {', '.join(map(str, lines))}")

    print(f"\n✅ Clean file saved as: {output_file}")


# Example usage:
remove_duplicate_ids("ar_DZ.lang")
