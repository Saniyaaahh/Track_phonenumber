# Phone Number Tracking System

## Overview

The **Phone Number Tracking System** allows you to track the location and carrier of any valid phone number by parsing the number with the help of the `phonenumbers` library. This tool is useful for identifying the origin and carrier of a phone number, which can be helpful in various situations, such as verifying phone numbers or obtaining region-specific information.

## Features

- **Location Tracking**: Get the geographic location of the phone number, such as the country or region.
- **Carrier Tracking**: Find the service provider associated with the phone number.
- **Error Handling**: Proper error messages for invalid phone numbers.

## Requirements

- Python 3.x
- `phonenumbers` library

## How to Use

1. Clone or download this repository to your local machine.
2. Ensure that you have Python 3.x and the `phonenumbers` library installed.
3. Run the Python script:

   ```bash
   python3 import_phonenumbers.py
   ```
4. When prompted, enter the phone number with the country code ```(e.g., +11234567890).```
5. The program will output the location and carrier of the phone number.

## Example Usage
```
Phone Number Tracking System
----------------------------
Enter the phone number with country code (e.g., +11234567890): +14155552671
Location: United States
Carrier: AT&T
```

## Error Handling
If the phone number is not in the correct format or is invalid, the system will return an error message prompting the user to include the country code. Example:

```
Error: Invalid phone number format. Please include the country code (e.g., +1 for USA).
```

## Author 
-  Yasmin Saniya Tabassum

## License
This project is licensed under the MIT License - see the LICENSE file for details.


