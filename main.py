import time
from plyer import notification


def water_reminder():
    while True:
        print("Sending water reminder notification...")
        notification.notify(
            title="Water Reminder",
            message="It's time to drink water! Stay hydrated.",
            app_name="Drink Water Reminder",
            timeout=10,
        )
        
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)


if __name__ == "__main__":
    water_reminder()