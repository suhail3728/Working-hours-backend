
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

# Basic Contribution guideline
# Contributions 

# Learning journal 



## Using React native use context. 

`useContext` is a react native hook that helps with accessing the value of a parameter from any screen under the same context without manually passing from each screens. 

### React native hooks 
Hooks are special functions in the react that helps in manage the states in different componets. Like useState hook , helps to change the variable state. useEffect hooks the functions will be called when the screen is loaded or when the value of variable is changed. 

While useing `useEffect(()=> randomFunctions(); {},[]); the codes in the the use effects runs the when the component loads. And if we are any variable inside the square bracket then the functions called inside the useEffect changes when the value of the variable changes like  `useEffect(()=> randomFunctions(); {},[userId]); , the codes inside the useEffect will be called whenever the value of the userId is changed.

These hooks can only be called inside a functional component in react. So a functional component is any javascript function that return jsx. Jsx is certain syntax of javascript where we create html like structues.

These hooks are very useful in my project, I use the useState to assign values to the variable. useEffects are used to show the ui according to the respective users. And the useContext was the one that helped me to pass parameters between different type of Stacks in my project.

### How it was useful in my project. 

So in react navigation happens by creating a navigation container that we can import from the package react-navigation and By creating Stack , where Stack is a `createStackNavigator` function we can import from react navigation. So we can create different `Stack.Navigator` inside the navigation container. And inside the `Stack.Navigators` we can use our screens by using `Stack.screen`.

So in my case I have two different types of stacks one is the AuthStack which have the screeens for user login or sign up and that is a `Stack.Navigator` and the other one is the userStack which contain the screens that the user will be using after authentication and that is a `Tab.navigator` where tab is a `createBottomTabNavigator` function that we import from `@react-navigation/bottom-tabs`. So I was troubling with moving how to move from the Stack navigator to the Tab navigator.

So I figured that out with the help of nested navigations from this article https://reactnavigation.org/docs/nesting-navigators/. by using the tab navigator as a component inside the stack navigator. And the next challege was how to pass the user id after authentication from the auth stack to userStack. Here evethough i am using the my bottoms tabs in userStack inside a stack navigator component, both are different files and different stacks. So I was struggling to find a way and then I found the `useContex` hook.

### How to use the `useContext` hook. 
```javascript

import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [userId, setUserId] = useState(null);
  const [emplyObject, setEmplyObject] = useState(null);
  const [emplyFlag, setEmplyFlag] = useState(null);

  return (
    <AuthContext.Provider value={{ userId, setUserId, emplyObject, setEmplyObject, emplyFlag, setEmplyFlag }}>
      {children}
    </AuthContext.Provider>
  );
};

```

So I first created a new file call `AuthContext` and we are exportinig two things from this file `AuthContext` and `AuthProvider`, these are the names give by me this can be any names. Here `Auth context` is the `createContext` function that the we import from react and `AuthProvider` is a functional component accepting a `childern` parameter. So I declared the `userId` and the `setUser Id` inside the `AuthProvider` and then the `AuthProvider` functional component is returning an `AuthContext.provider` where you can define the values that the childern of this can be used, in my case i have the `userId` and the `setUser` function inside the `value` so that any of the children element can use these. 

Then after creating the `AuthContext` file, I wrapped my Navigation container in the `App.js` file with the `AuthProvider` and then I imported the `setUserId` function in the usercreation page in the `AuthStack` and set the value for the `userId` and then when I move to the `userStack` I import the `userId` from the `AuthContext` and userthe `userId`. This is possible because as we wrapped our main navigator inside the `AuthProvider` and we can set or use the `userId` value from any screens inside the children of the `AuthProvider`, this was very useful. 


### Resources that helped me : 

* Crawford, T. (2023, September 22). React Navigation - Nesting Navigators. YouTube. https://www.youtube.com/watch?v=6RhOzQciVwI
* NetNinja (2020). React Context & Hooks. YouTube. https://www.youtube.com/watch?v=-40TBdSRk6E
* React Navigation. (n.d.). Nesting navigators. Retrieved October 25, 2024, from https://reactnavigation.org/docs/nesting-navigators/
