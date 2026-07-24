import re

text = """
You can contact us at support@gmail.com or help@yahoo.com.

John's phone number is 98765-43210.
Alice's phone number is 91234-56789.
"""

emailRegex = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
phoneRegex = re.compile(r'\d{5}-\d{5}')

emails = emailRegex.findall(text)
phones = phoneRegex.findall(text)

print("Emails Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)