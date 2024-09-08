from twilio.rest import Client
import random
import time

# Twilio Account SID and Auth Token (replace with your credentials)
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_random_sms(phone_number, interval=2):
    """
    Function to send random SMS messages using Twilio API.

    :param phone_number: str - The target phone number (in international format).
    :param interval: int - Time delay between messages (in seconds).
    """
    messages = [
        "Hey! Don't forget to stay hydrated today.",
        "Reminder: Take a short break and stretch.",
        "Hope you're having a great day!",
        "Quick tip: Set your daily goals and crush them!"
    ]

    try:
        while True:
            # Select a random message from the list
            message_body = random.choice(messages)

            # Send SMS using Twilio API
            message = client.messages.create(
                body=message_body,
                from_='',  # Replace with your Twilio number
                to=phone_number
            )
            print(f"Sent message: '{message_body}' to {phone_number}")

            # Delay before sending the next message
            time.sleep(interval)

    except Exception as e:
        print(f"Error occurred: {e}")
    except KeyboardInterrupt:
        print("\nScript stopped manually.")

if __name__ == "__main__":
    # Replace 'YOUR_TARGET_NUMBER' with the phone number you want to send SMS to
    target_number = 'YOUR_TARGET_NUMBER'

    # Customize time interval between messages (in seconds)
    send_interval = 5

    send_random_sms(target_number, send_interval)
