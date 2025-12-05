def load_keys(file_path):
    keys = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            original = line.rstrip("\n")
            stripped_line = original.strip()
            if "=" in stripped_line:
                key = stripped_line.split("=", 1)[0].strip()
                if key:
                    keys[key] = (original, i)  # store the full line and line number
    return keys


def compare_files(file1, file2):
    keys1 = load_keys(file1)
    keys2 = load_keys(file2)

    added_keys = keys2.keys() - keys1.keys()
    removed_keys = keys1.keys() - keys2.keys()

    print("New lines (Green):")
    for key in sorted(added_keys):
        line, line_num = keys2[key]
        print(f"\033[92m+ Line {line_num}: {line}\033[0m")

    print("\nDeleted lines (Red):")
    for key in sorted(removed_keys):
        line, line_num = keys1[key]
        print(f"\033[91m- Line {line_num}: {line}\033[0m")


# Example usage:
# To use this, create two files named 'en_US.lang' and 'ar_DZ.lang'
# with some differing key=value pairs.
# For example:
# en_US.lang:
# key1=Hello
# key2=World
#
# ar_DZ.lang:
# key1=مرحباً
# key3=عالم

# The following call is commented out to prevent execution errors without the files.
compare_files("en_US.lang", "ar_DZ.lang")
