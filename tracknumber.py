import phonenumbers
from phonenumbers import geocoder, carrier

def track_phone_number(phone_number):
    """Tracks the location and carrier of a given phone number."""
    try:
        parsed_number = phonenumbers.parse(phone_number)

        # Get location information
        location = geocoder.description_for_number(parsed_number, "en")

        # Get carrier information
        service_provider = carrier.name_for_number(parsed_number, "en")

        return {
            "Location": location if location else "Unknown",
            "Carrier": service_provider if service_provider else "Unknown"
        }

    except phonenumbers.NumberParseException:
        return {
            "Error": "Invalid phone number format. Please include the country code (e.g., +1 for USA)."
        }

if _name_ == "_main_":
    print("Phone Number Tracking System")
    print("----------------------------")

    # Get user input
    phone_number = input("Enter the phone number with country code (e.g., +11234567890): ")

    # Track the phone number
    result = track_phone_number(phone_number)

    # Display the result
    for key, value in result.items():
        print(f"{key}: {value}")