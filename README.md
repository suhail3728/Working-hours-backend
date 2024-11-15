    # Project Overview
A team management solution designed for business organizations to efficiently organize and manage their workforce. The platform serves two distinct user types: Business Owners and Workers.
<detatils>
<summary> User documentation</summary>

## User Types
### 1. Business Owner
The primary administrator who manages the business and team operations.

### 2. Worker
Employees hired by the business owner who need to view their work schedules.

## Key Features

### For Business Owners

#### Business Setup
- Create an account with business and personal information
- Receive a unique business ID (required for worker registration)
- Access business ID through the settings page

#### Organization Management
- Create and manage departments (e.g., Kitchen, Front House)
- Define roles within each department (e.g., Prep Cook, Line Cook, Dishwasher)
- Manage team structure and hierarchy

#### Team Management
- Add team members to the organization
    - **Worker's email address (must be collected during hiring)**
    - Department assignment
    - Role assignment
  - Share business ID with workers during onboarding

#### Shift Management
- Create and assign shifts to team members
- Specify departments and roles for each shift
- Set schedule start and end times

### For Workers

#### Account Creation
- Register using:
  - Email address (provided to business owner)
  - Business ID (provided by owner during hiring)

#### Shift Access
- View personally assigned shifts
- Access schedule details including:
  - Department
  - Role
  - Start time
  - End time

## Workflow Summary
1. Owner sets up business profile
2. Owner creates departments and roles
3. Owner adds team members
4. Owner creates and assigns shifts
5. Workers register and access their schedules
</details>



# Installation Steps
 ## How to install react-native

 ### Required tools

- Node.js

We can download the node.js from the following we need version 16 or higher.
  ```
  https://nodejs.org/en
```

- Java Development Kit 

We need the jdk version 17 which can be downloaded from the Oracle website.
```
https://www.oracle.com/java/technologies/downloads/
```
- Android Studio 

Android studio can be downloaded from the link below. While installing this we will get the android sdk required for building android applications

```
https://developer.android.com/studio
```


- create new project 

```
npx react-native@latest init YourProjectName
```

run this in the command prompt to create a new project and the react-native is ready to develop.

 ## How to install flask

1. Install the latest version of the python 
```
https://www.python.org/downloads/
```
2. Create a virtual environment

```
python -m venv venv
```

3. Create a folder (Like MyflaskApp)  and install the necessary packages

```
pip install flask
pip install flask-cors
pip install python-dotenv
pip install flask-cors
```

4. Wrap the application in the CORS( Cross-Origin Resource Sharing) for using the Flask app for the react-native project.
```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/api/hey')
def example_route():
    return jsonify({"message": "Hey"})

if __name__ == '__main__':
    app.run(debug=True)
```
5. Run the app

Run the following command in the flask project directory now the app is ready to use. We can check by giving the sample api created above.

```
python app.py
```


## SetUp the firebase account

1. Create a project in firebase 

```
https://console.firebase.google.com/u/0/
```
2. Create a new web app
   Create a new web app in the Firebase copy the configurations and paste that into a config.js file react-native project download the JSON that we receive at the end of creating the app and add that to the flask app.
# Usage Instructions
there will be two types of users one as a business owner/ manager or as a worker

## Owner user instructions:
### 1.Creating new account:
1. Press the button `I'm new to workingHours`.
2. Press the `Create a team` button.
3. Complete the four user creation steps to create the account and will be redirected to the homepage.
### 2.Creating new department:   
1. Go to the options tab, which is the last tab in the bottom navigations with a hamburger icon.
2. Select the Departments and roles section.
3. Press the Edit button on the top right corner.
4. Press the plus buttons to create departments.
5. Press the nested plus buttons inside under each department to create new roles.
   ### 3.Creating new team member:
1. Go to the options tab, which is the last tab in the bottom navigations with a hamburger icon.
2. Press the floating action plus button go to create new team members.
3. Create a new team member by filling the input fields

  ### 4. Creating new shifts:
   1. Go to the shifts tab which is the second bottom tab.
   2. Press the `Create new shift` button.
   3. Create the new shift by filling the inputs.

### Sharing the business key for the employees

The new hires need the business key from the owner user to verify and create the account.

1. Go to the options tab in the bottom navigations. That is the last tab with the hamburger icon.
2. Press the business ID on the top under the profile. It will automatically copy the business Id and share this to the employees to join the team.
 

## Owner user instructions:

### 1.Creating new account:
You should receive the business key from the employer to create an account
1. Press the button `I'm new to workingHours`.
2. Press the `Join a team ` button.
3. Provide the email and the business is provided by the employer and press the verify button.
4. After verification create a password and will be redirected to the home page.

### 2. View the shifts

1. Go to the home page and will see the shifts assigned to you
2. Go to the shifts tab which is the second tab to see the details of all the shifts in your working place.



