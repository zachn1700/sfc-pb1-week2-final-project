from datetime import datetime, timezone

def export_report(sat_data, filename="output/report_output.txt"):
    with open(filename, "w") as f:
        # 1. Determine stale state tag status. If older than 48 hours data will be stale, see parser.py
        if sat_data["is_stale"]:
            status_tag = "[STALE DATA]"
        else:
            status_tag = "[CURRENT DATA]"

        # 2. Format age string
        if sat_data["age_hours"] is not None:
            rounded_age = round(sat_data["age_hours"], 1)
            age_str = f"{rounded_age}"
        else:
            age_str = "Unknown"

        # 3. Format epoch date string
        if sat_data["epoch"] is not None:
            epoch_str = sat_data["epoch"].strftime("%Y-%m-%d %H:%M:%S ZULU")
        else:
            epoch_str = "Unknown"

        # Formats and prints the actual output file
        border = "=" * 70
        small_border = "-" * 70
        generated_dtg = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S ZULU")

        # Header
        f.write(f"{border}\n")
        f.write(f"{sat_data['name'].center(70)}\n")
        f.write(f"{border}\n")

        # Sat Info block
        left_col_ssc = f"NORAD / SSC: {sat_data['ssc']}"
        f.write(f" {left_col_ssc:<40} DATA STATUS: {status_tag}\n")

        left_col_epoch = f"EPOCH TIME : {epoch_str}"
        f.write(f" {left_col_epoch:<40} DATA AGE: {age_str} HOURS OLD\n")

        # TLE Block
        f.write(f"{small_border}\n")
        f.write(" [SPACES MARKED WITH '*']\n")
        f.write(f" {sat_data['line1'].replace(' ', '*')}\n")
        f.write(f" {sat_data['line2'].replace(' ', '*')}\n")
        f.write(f"{small_border}\n")

        # Footer
        f.write(f" REPORT GENERATED AT DTG: {generated_dtg}\n")
        f.write(f"{border}\n")


    print(f"[+] Saved report to: {filename}")

    with open(filename, "r") as f:
        print("\n" + f.read())
    return
