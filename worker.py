import os
import time
import requests

# Replace with your target URL
url = "https://speak-slowly.loca.lt"

while True:
    try:
        # Send the GET request
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            print("GET request successful!")
        else:
            print(
                f"GET request failed with status code {response.status_code}")
            os.system('lt --port 5002 --subdomain speak-slowly')

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Sleep for 300 seconds before sending the next request
    time.sleep(5)
