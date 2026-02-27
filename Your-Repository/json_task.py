import json
import os


# --- FILE PATH (always works) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "sample-data.json")


def load_json():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_interfaces(data):
    rows = []

    imdata = data.get("imdata", [])

    for item in imdata:
        for key in item:
            attributes = item[key].get("attributes", {})

            dn = attributes.get("dn", "")
            mtu = attributes.get("mtu", "")
            speed = attributes.get("fecMode", "")

            if dn and mtu:
                rows.append((dn, speed, mtu))

    return rows


def print_table(rows):
    print("Interface Status")
    print("=" * 90)
    print(f"{'DN':60} {'Speed':15} {'MTU':10}")
    print("-" * 90)

    for dn, speed, mtu in rows:
        print(f"{dn:60} {speed:15} {mtu:10}")


def main():
    try:
        data = load_json()
        rows = extract_interfaces(data)
        print_table(rows)
    except FileNotFoundError:
        print("ERROR: sample-data.json file not found.")


if __name__ == "__main__":
    main()