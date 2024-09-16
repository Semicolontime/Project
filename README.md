# Site entry form
#### Video Demo: <URL HERE>
#### Description:
# Simple Website Login System

Welcome to the Simple Website Login System project! This Python application simulates a basic website login page with a variety of features, all developed using Python alone.

## Overview

The application includes:

- **8 Functions**
- **2 Classes**

### Functions

1. **`main`**: This is the entry point of the application. Running this function starts the program.

2. **`sign_up`**: This function handles user registration. When executed, it prompts the user to enter a username and a password. Passwords are checked against a regex pattern to ensure they meet complexity requirements. Users must choose a valid password to proceed with registration.

3. **`log_in`**: After registration, users can log in using this function. It first asks for the username. If the username is incorrect, the user is redirected to the sign-up page. If the username is correct, the function then asks for the password. If the password is incorrect, the user has the option to either re-enter it or use the "forgot_password" feature.

4. **`forgot_password`**: If users forget their password, this function allows them to recover it. It asks for a phone number, which is validated using regex for Iranian phone formats. A default recovery code (232323) is used to simulate the recovery process. Entering the correct code will allow users to access their account.

5. **`options`**: This is the main interactive function that presents users with various features:

   - **Calculator**: A simple calculator that performs basic arithmetic operations. The `use_calculator` function handles the calculations based on user input and displays the result.
   
   - **Cow Say**: This feature lets users display a message in a speech bubble from a selected animal using the `cowsay` library. The `cow_say` function manages the visual output.

   - **Bank Account**: Simulates a bank account with a wallet interface. Users can deposit, withdraw, and check their balance using a class designed to manage the wallet's balance.

   - **Cookies**: Allows users to create and manage a virtual cookie jar. Users can define and adjust the number of cookies using the `Jar` class.

   - **Bitcoin Price**: Fetches and displays the current price of Bitcoin. It uses the `requests` and `json` libraries to get the price and `pyttsx3` to read it out loud.

6. **`line`**: Adds decorative lines to enhance the terminal interface.

## How to Use

1. Start by running the `main` function to launch the application.
2. Follow the prompts to register, log in, and explore the various features available.

## Dependencies

To run this project, you'll need the following Python libraries:

- `requests`
- `json`
- `pyttsx3`
- `cowsay`
- `re` (for regex validation)

