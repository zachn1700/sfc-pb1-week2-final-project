from datetime import datetime, timedelta, timezone

def calculate_epoch_date(line1):
    # TLEs have a standard format. This slices TLEs to grab certain indexes in order to parse that into useable data, like calculating the time/date
    epoch_string = line1[18:32].strip()
    year = int(epoch_string[:2])
    day = float(epoch_string[2:])

    # Math to convert 1900s vs 2000s. If greater than 57 it was in the 1900s, if lower it's in the 2000s
    if year >= 57:
        year += 1900
    else:
        year += 2000

    # Creates a starting point for our time calculation. Starts Jan 1st so we can add or subtract our epoch time off of it. Also ensures we use UTC/ZULU time and not local time
    base_date = datetime(year, 1, 1, tzinfo=timezone.utc)
    epoch_date = base_date + timedelta(days = day -1)
    return epoch_date


# Cleans and parses each line of TLE data, stores parsed data in a var and returns a dictionary for output
def parse_tle(tle_lines):
    if not tle_lines or (len(tle_lines)) < 3:
       # print(f'Invalid TLE')
        return None

    sat_name = tle_lines[0].strip()
    line1 = tle_lines[1].strip()
    line2 = tle_lines[2].strip()
    ssc = line1[2:7].strip()

    epoch_date = calculate_epoch_date(line1)

    current_time = datetime.now(timezone.utc)
    time_difference = current_time - epoch_date
    age_in_hours = time_difference.total_seconds() / 3600.0

    is_stale = age_in_hours > 48.0

    return {
        "name": sat_name,
        "line1": line1,
        "line2": line2,
        "epoch": epoch_date,
        "age_hours": age_in_hours,
        "is_stale": is_stale,
        "ssc": ssc
    }