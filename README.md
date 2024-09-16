# Site Entry Form

#### Video Demo: <URL HERE>

#### Description:

This program is a simple design of a website login page. Once logged in, you will have access to various features. This project demonstrates a website login system with multiple functionalities, all developed using Python.

### Program Details:

The program is composed of 8 functions and 2 classes. Here is a brief overview of each component:

1. **`main`**:
   - The main function that starts the execution of the project.

2. **`sign_up`**:
   - Manages user registration by requesting a username and password. The password is validated using regex to prevent simple passwords. Users must enter a password that meets the defined criteria to proceed.

3. **`log_in`**:
   - Handles user login. It first asks for the username. If the username is incorrect or not registered, the user is prompted to sign up again. If the username is correct, the function requests the password. The user can enter the password once and, if forgotten, has the option to use the `forgot_password` function.

4. **`forgot_password`**:
   - Requests the user’s phone number to send a recovery code. The phone number is validated using regex for Iranian numbers. A default recovery code (232323) is sent, which the user must enter to retrieve their password and access the main site.

5. **`options`**:
   - The main function providing various features:
     - **Calculator**: Allows the user to perform four basic arithmetic operations. The user is redirected to the `use_calculator` function to choose an operation, input values, and view results.
     - **Text by Animal**: Lets the user input a sentence and choose an animal. The selected animal will "speak" the sentence using the `cowsay` library.
     - **Bank Account Recharge**: Represents a symbolic wallet on the site. Users can manage their wallet balance, including deposits and withdrawals, through a dedicated class.
     - **Cookie Jar**: Allows users to define and manage a specific number of cookies. This is handled by the `Jar` class, which lets users add or remove cookies.
     - **Bitcoin Price**: Displays the current price of Bitcoin. It uses the `requests` and `json` libraries to fetch the price and the `pyttsx3` library to read it out loud.

6. **`line`**:
   - Adds a decorative line in the terminal to improve visual separation between sections.

This project simulates a website login and user account management system. We hope you find the details clear and encourage you to test the project.
