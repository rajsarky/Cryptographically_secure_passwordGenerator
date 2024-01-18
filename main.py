import secrets
import string

generated_passwords = set()
def generate_random_password(length=12):
  """Generates a random password with the specified length using cryptographically secure randomness.

  Args:
    length: The desired length of the password (default: 12).

  Returns:
    A string containing a randomly generated password.
  """

  # Character sets for password generation
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  # Combine character sets for diversity
  all_chars = lower + upper + digits + punctuation

  # Create an empty set to store generated passwords

  while True:
    # Generate a random password using secrets.token_urlsafe()
    password = ''.join(secrets.choice(all_chars) for _ in range(length))

    # Check if the password is already generated
    if password not in generated_passwords:
      generated_passwords.add(password)  # Add to the set to prevent repetition
      return password

# Example usage

print("How long do you want the password to be?")
length = int(input())
password = generate_random_password(length)
print(password)  # Output: e.g., "s9^54-eK&54a-54a54F"
