# importing the required libraries used in the file
from flask import render_template, request, jsonify
from backend import app, db
from backend.models import User

@app.route("/")
def home():
    return "hello"

# Define a route for the /api/sos endpoint
@app.route('/sos', methods=['POST'])
def send_fake_sos_alert():
    # Get data from the request, including location
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    # Simulate sending an SOS alert (replace with your logic)
    fake_phone_number = '555-1234'
    fake_message = f"SOS Alert! Location: Lat {latitude}, Long {longitude}"
    print(fake_message)
    # You can replace this with actual SMS sending logic or other actions
    response = {'status': 'success', 'message': 'Fake SOS alert sent.'}
    return jsonify(response)

unsafe_zones = [
    {"name": "Unsafe Zone 1", "latitude": 40.7128, "longitude": -74.0060},
    # Add more unsafe zones as needed
]

# a route endpoint for checking whether a zone is safe or not
@app.route('/check-unsafe-zone', methods=['POST'])
def check_unsafe_zone():
    data = request.get_json()
    user_latitude = data.get('latitude')
    user_longitude = data.get('longitude')

    # Check if the user's location is within any unsafe zone
    alert_message = None
    for zone in unsafe_zones:
        if (
            abs(user_latitude - zone['latitude']) < 0.01 and
            abs(user_longitude - zone['longitude']) < 0.01
        ):
            alert_message = f"You are in an unsafe zone: {zone['name']}"
            break

    response = {'alertMessage': alert_message}
    return jsonify(response)

