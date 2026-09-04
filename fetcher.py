import urllib.request

def fetch_tle(ssc_id):
    # Grab the desired sat SSC and strip any whitespaces from the input
    clean_id = str(ssc_id).strip()

    # We're going to use an open source site called celestrak to grab TLEs from. This inputs the clean_id into the URL where the NORAD/SSC number would normally go
    url = f'https://celestrak.org/NORAD/elements/gp.php?CATNR={clean_id}&FORMAT=tle'

    # This is to make our web request look like a normal web browser and not a bot/python script. A lot of websites will reject URL requests from bots
    headers = {"User-Agent": "Mozilla/5.0"}
    request_object = urllib.request.Request(url, headers=headers)

    try:
        # Open the connection to the URL (wait up to 10 seconds). Error if no response from Celestrak within 10 seconds
        with urllib.request.urlopen(request_object, timeout=10) as response:

            # Receives the raw data from Celestrak, decodes it into human readable characters, and then removes any extra whitespaces in the data
            raw_bytes = response.read()
            text = raw_bytes.decode("utf-8")
            clean_text = text.strip()

            # If SSC isn't in Celestrak's database, return this
            if "No GP data found" in clean_text or clean_text == "":
                print(f'No satellite data found for {ssc_id}')
                return None

            # Splits the block of text into separate lines
            lines = clean_text.splitlines()
            return lines

    # Catch all for errors so the program doesn't crash
    except Exception:
        #print(f'An error occurred, please try again')
        return None