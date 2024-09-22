from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import random
import time
import threading
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Twilio Account SID and Auth Token (from environment variables)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)

# Global variables
send_sms_flag = False
active_thread = None
current_messages = []

def validate_phone_number(phone_number):
    """Validate phone number format."""
    pattern = re.compile(r'^\+\d{10,14}$')
    return bool(pattern.match(phone_number))

def send_random_sms(phone_number, interval):
    global send_sms_flag, current_messages

    while send_sms_flag and current_messages:
        message_body = random.choice(current_messages)
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=phone_number
            )
            print(f"Sent message: '{message_body}' to {phone_number} (SID: {message.sid})")
        except TwilioRestException as e:
            print(f"Twilio Error: {e}")
            send_sms_flag = False
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            send_sms_flag = False
            break

        time.sleep(interval)

@app.route('/start', methods=['POST'])
def start_sms():
    global send_sms_flag, active_thread, current_messages

    if send_sms_flag:
        return jsonify({"message": "SMS sending already in progress."}), 400

    data = request.get_json()
    phone_number = data.get('phone')
    interval = data.get('interval')
    messages = data.get('messages', [])

    if not phone_number or not interval:
        return jsonify({"message": "Missing phone number or interval."}), 400

    if not validate_phone_number(phone_number):
        return jsonify({"message": "Invalid phone number format."}), 400

    try:
        interval = int(interval)
        if interval < 1 or interval > 3600:
            return jsonify({"message": "Interval must be between 1 and 3600 seconds."}), 400
    except ValueError:
        return jsonify({"message": "Invalid interval value."}), 400

    if not messages:
        return jsonify({"message": "No messages provided."}), 400

    current_messages = messages
    send_sms_flag = True
    active_thread = threading.Thread(target=send_random_sms, args=(phone_number, interval))
    active_thread.start()

    return jsonify({"message": f"Started sending SMS to {phone_number} every {interval} seconds."}), 200

@app.route('/stop', methods=['POST'])
def stop_sms():
    global send_sms_flag, active_thread

    if not send_sms_flag:
        return jsonify({"message": "No active SMS sending process."}), 400

    send_sms_flag = False
    if active_thread:
        active_thread.join(timeout=5)  # Wait for the thread to finish
        active_thread = None

    return jsonify({"message": "Stopped sending SMS."}), 200

@app.route('/status', methods=['GET'])
def get_status():
    global send_sms_flag
    status = "active" if send_sms_flag else "inactive"
    return jsonify({"status": status}), 200

if __name__ == '__main__':
    app.run(debug=True)
