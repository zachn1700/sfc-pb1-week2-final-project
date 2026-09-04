"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""
from fetcher import fetch_tle
from parser import parse_tle
from exporter import export_report

def display_menu():
    """
    Show the main menu to the user.
    Customize this for your application.
    """
    print("\n" + "="*40)
    print("SATELLITE EPHEMERIS (TLE) FETCHER".center(40))
    print("="*40)
    print("1. Fetch TLEs by NORAD/SSC")
    print("help - Show this menu")
    print("quit or 'q' - Exit application")
    print()


def handle_choice(choice):
    """
    Process the user's choice and call appropriate functions.

    Args:
        choice (str): The user's input

    Returns:
        bool: True to continue, False to exit
    """
    if choice == "1":
        while True:
            ssc_input = input("\nEnter NORAD/SSC Number (or 'c' to cancel): ").strip()

            if ssc_input.lower() == "c" or ssc_input.lower() == "cancel":
                print("[*] Operation canceled.")
                display_menu()
                break

            raw_lines = fetch_tle(ssc_input)

            if raw_lines is None:
                print(f"[!] Invalid or unavailable SSC '{ssc_input}'. Try again.")
                continue

            sat_data = parse_tle(raw_lines)
            if sat_data is None:
                print(f"[!] Failed to parse element set for SSC '{ssc_input}'. Try again.")
                continue

            export_report(sat_data)
            continue

    elif choice == "help":
        display_menu()

    elif choice == "quit" or choice == 'q':
        print("\nThanks for using the application. Goodbye!")
        return False

    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")

    return True

def main():
    """
    Main application loop.
    Displays menu, gets user input, processes choices.
    """
    display_menu()

    running = True
    while running:
        choice = input("\nEnter your choice: ").strip().lower()
        running = handle_choice(choice)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Operation terminated by operator. Exiting...")

# TODO
# Batch processing multiple SSCs at once
# "Sat presets" to "save" multiple sats in a list/preset and query/batch process
# them at once.
#
#
#
