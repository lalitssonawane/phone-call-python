from twilio.rest import TwilioRestClient
TWILIO_PHONE_NUMBER = ""
DIAL_NUMBERS = ["",]
TWIML_INSTRUCTIONS_URL = \
client = TwilioRestClient("ACxxxxxxxxxx", "yyyyyyyyyy")


def dial_numbers(numbers_list):
    for number in numbers_list:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)