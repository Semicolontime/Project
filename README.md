# Site Entry Form

#### Video Demo: <URL HERE>

#### Description:

This program is a simple design of a website login page. After logging in, you will have access to limited and defined features. Essentially, this project implements a website login with various features, all developed using Python only.

### Program Details:

The program consists of 8 functions and 2 classes. Here is an overview of each component:

1. **`main`**:
   - This is the main function of the program and initiates the execution of the project.

2. **`sign_up`**:
   - This function handles user registration. It prompts the user for a username and a password. The password is validated using regex to prevent simple passwords. Users cannot proceed to the next step until they enter a password that meets the defined criteria.

3. **`log_in`**:
   - This function is used when the user wants to log into their account after completing the registration. It first requests the username. If the username is incorrect or the user is not registered, they are prompted to sign up again. If the username is correct, the function then asks for the password. The user can enter the password once, and if they forget it, they have the option to execute the `forgot_password` function.

4. **`forgot_password`**:
   - This function asks the user for their phone number to send a recovery code. The phone number is validated using regex for Iranian phone numbers. After entering the phone number, a default recovery code (232323) is sent. The user needs to enter this code to retrieve their password and then access the main site.

5. **`options`**:
   - This is the main function that provides various features to the user. Based on the selected option, different functions are called:
     - **Calculator**: This feature allows the user to perform four basic arithmetic operations. The user is redirected to the `use_calculator` function where they can choose an operation, input values, and see the result.
     - **Text by Animal**: With this option, the user can input a sentence and choose an animal. The chosen animal will then "speak" the sentence using the `cowsay` library.
     - **Bank Account Recharge**: This feature represents a symbolic wallet on the site. Users can manage their wallet balance, including depositing and withdrawing funds, through a specific class designed for this purpose.
     - **Cookie Jar**: Users can define and manage a specific amount of cookies. This functionality is handled by the `Jar` class, allowing users to add or remove cookies.
     - **Bitcoin Price**: This feature displays the current price of Bitcoin. It uses the `requests` and `json` libraries to fetch the price and the `pyttsx3` library to read it out loud.

6. **`line`**:
   - This function adds a decorative line in the terminal to enhance the visual separation of different sections.

This project represents a simulated website login and user account management system. I hope you understand the details and encourage you to test the project.
