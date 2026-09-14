from datetime import datetime


def generate_log(data):
    """
    Write a list of log entries to a dated .txt file.

    Args:
        data (list): log entries to write, one per line.

    Returns:
        str: the filename the log was written to (e.g. "log_20260914.txt").

    Raises:
        ValueError: if data is not a list.
    """

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list of log entries")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)