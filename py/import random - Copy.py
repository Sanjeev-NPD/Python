import random
import string

def generate_random_email():
    # Generate a random string of letters and digits for the username part
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # Choose a random email domain from a list
    email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    domain = random.choice(email_domains)

    # Combine username and domain to form the email ID
    email = f'{username}@{domain}'

    return email

# Generate 4 random email IDs
for _ in range(4):
    random_email = generate_random_email()
    print(random_email)
