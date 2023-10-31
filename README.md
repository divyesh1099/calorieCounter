# Calorie Counter

An intuitive and user-friendly web application to keep track of daily calorie intake and maintain a healthier lifestyle.

## Table of Contents

1. [Introduction](#introduction)
2. [Screenshots](#screenshots)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Introduction

Calorie Counter allows users to log their daily food items and calculates the total calorie intake, helping them manage and achieve their dietary goals.

## Screenshots

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/f2e20a75-3620-444c-9d2c-6fd650b5431b)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/42b40237-496e-4cb7-bc9f-1b72d6631b92)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/d699607e-f1af-4495-ab91-3d7787b04bf2)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/14e1bdf6-585f-4871-9d50-7a3c98455ae6)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/7f188d17-53dd-4f16-af6a-ca0b7b044062)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/cbb8af02-437a-4157-80a5-d8379c219d5b)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/b9a37da1-be66-4655-958e-d0bc75aeedef)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/3fa17932-76cd-4d26-8c6c-a4cc6a71be48)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/cd0e641c-4e0c-4525-b306-62302e7aad16)

![image](https://github.com/divyesh1099/calorieCounter/assets/65925922/3197cebf-ca43-4228-b8a8-6306b2854f0c)

## Features

### User Authentication
Our platform prioritizes user experience and security:
- **Sign Up**: New to the app? Quickly create an account using just an email address and password. Our registration process is streamlined for efficiency.
- **Log In**: Returning users can easily log in to access their personalized dashboard, which stores and displays their calorie tracking history and preferences.
- **Profile Management**: Users can edit their profile, change their password, and manage other personal settings for a tailored experience.

### Food Database
Dive into our extensive collection of food items:
- **Search & Select**: Easily browse through thousands of foods, each listed with their specific calorie values. Our robust search functionality ensures you can find what you're looking for in seconds.
- **Nutritional Details**: Alongside calorie count, access other nutritional details to understand more about your food choices.

### Daily Intake Tracker
Track every bite:
- **Log Your Meals**: With just a few taps, add food items to your daily log. Whether it's breakfast, lunch, dinner, or snacks in between – we've got you covered.
- **Timestamped Entries**: Each entry is timestamped, allowing you to understand your eating patterns better.

### Dynamic Updating
Instant insights:
- **Real-time Calculation**: As you log your meals, watch your total calorie count adjust in real-time, ensuring you always know where you stand against your daily goals.
- **Visual Feedback**: Get instant visual feedback on your dashboard, helping you make immediate and healthy decisions.

### Reports
Deep dive into your dietary patterns:
- **Real-time Analysis**: Access reports that instantly update as you add or modify entries. Stay informed with the most current data.
- **Historical Data**: View past daily, weekly, or monthly reports to understand trends and make informed dietary decisions.
- **Graphs & Charts**: Visual representations to make data interpretation easy and intuitive.

### Recipe Database
Inspiration for your next meal:
- **Diverse Collection**: Browse through a variety of recipes, from comfort food to gourmet dishes.
- **Calorie Information**: Every recipe comes with total calorie count and breakdown by ingredients, helping you make informed meal choices.
- **User Contributions**: Love a recipe? Share it with the community! Add your own recipes and let others benefit from your culinary adventures.

### Automatic Food Addition
Staying comprehensive and current:
- **FDA API Integration**: Can't find a food item? Our system automatically queries the FDA's extensive food database using its API.
- **Automatic Updates**: As soon as a new food item is found in the FDA database, it's added to ours. This ensures our food database is always comprehensive and up-to-date.

## Technologies Used

- **Backend**: Django 4.2.4
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap

## Setup and Installation

1. **Clone the Repository**

```bash
git clone <repository-url>
cd caloriecounter
```

2. **Install Dependencies**

Ensure you have Python 3.11 installed. Then:

```bash
pip install -r requirements.txt
```

3. **Database Setup**

(Mention how to set up the database, any migrations)

```bash
python manage.py migrate
```

4. **Start the Server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

### **Getting Started**

1. **User Authentication**:
   - **Sign Up**: Register for an account using a valid email address.
   - **Log In**: Access your personalized dashboard using your credentials.

### **Tracking Your Calories**

2. **Daily Intake Tracker**:
   - Navigate to the 'Daily Tracker' section.
   - Log each food item you consume throughout the day.
   - Monitor your total calorie intake as it updates in real-time.

3. **Food Database**:
   - Browse through our extensive food database to find calorie values of various items.
   - Search for specific food items using the search bar.

4. **Automatic Food Addition**:
   - Can't find a food item? Don't worry! 
   - The app uses the FDA API to automatically search and add items to the database, ensuring it stays up-to-date.

### **Recipes & Meal Planning**

5. **Recipe Database**:
   - Explore a variety of recipes stored in our database.
   - Check out each recipe's ingredients and total calorie count.
   - Add your own favorite recipes for others to try!

### **Insights & Reports**

6. **Dynamic Updating**:
   - Keep an eye on the top of your dashboard.
   - Watch as your total calorie count updates dynamically with each food item you log.

7. **Reports**:
   - Visit the 'Reports' section to get insights into your eating habits.
   - Track your daily, weekly, or monthly calorie intake.
   - Make informed decisions based on your consumption patterns.

## Contributing

Contributions are always welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started. Please adhere to this project's `code of conduct`.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Created by [Divyesh Nandlal Vishwakarma](https://www.linkedin.com/in/divyesh-vishwakarma-621197175/) - feel free to contact me at [divyesh1099@gmail.com](mailto:divyesh1099@gmail.com)!
