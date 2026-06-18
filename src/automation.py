from datetime import datetime


def write_log(message):

    with open(
        "logs/system.log",
        "a"
    ) as file:

        timestamp = datetime.now()

        file.write(
            f"[{timestamp}] "
            f"{message}\n"
        )
def log_system_completion():

    write_log(
        "RetailIQ executed successfully."
    )