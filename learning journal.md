# Learning journal 

<details>
<summary>  Using React native use context</summary>

## Using React native use context
`useContext` is a react native hook that helps with accessing the value of a parameter from any screen under the same context without manually passing from each screens. 

### React native hooks 
Hooks are special functions in the react that helps in manage the states in different componets. Like useState hook , helps to change the variable state. useEffect hooks the functions will be called when the screen is loaded or when the value of variable is changed. 

While useing `useEffect(()=> randomFunctions(); {},[]);` the codes in the the use effects runs the when the component loads. And if we are any variable inside the square bracket then the functions called inside the useEffect changes when the value of the variable changes like  `useEffect(()=> randomFunctions(); {},[userId]); , the codes inside the useEffect will be called whenever the value of the userId is changed.

These hooks can only be called inside a functional component in react. So a functional component is any javascript function that return jsx. Jsx is certain syntax of javascript where we create html like structues.

These hooks are very useful in my project, I use the useState to assign values to the variable. useEffects are used to show the ui according to the respective users. And the useContext was the one that helped me to pass parameters between different type of Stacks in my project.

### How it was useful in my project

So in react navigation happens by creating a navigation container that we can import from the package react-navigation and By creating Stack , where Stack is a `createStackNavigator` function we can import from react navigation. So we can create different `Stack.Navigator` inside the navigation container. And inside the `Stack.Navigators` we can use our screens by using `Stack.screen`.

So in my case I have two different types of stacks one is the AuthStack which have the screeens for user login or sign up and that is a `Stack.Navigator` and the other one is the userStack which contain the screens that the user will be using after authentication and that is a `Tab.navigator` where tab is a `createBottomTabNavigator` function that we import from `@react-navigation/bottom-tabs`. So I was troubling with moving how to move from the Stack navigator to the Tab navigator.

So I figured that out with the help of nested navigations from this article https://reactnavigation.org/docs/nesting-navigators/. by using the tab navigator as a component inside the stack navigator. And the next challege was how to pass the user id after authentication from the auth stack to userStack. Here evethough i am using the my bottoms tabs in userStack inside a stack navigator component, both are different files and different stacks. So I was struggling to find a way and then I found the `useContex` hook.

### How to use the `useContext` hook

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

### Resources that helped me

* Crawford, T. (2023, September 22). React Navigation - Nesting Navigators. YouTube. https://www.youtube.com/watch?v=6RhOzQciVwI
* NetNinja (2020). React Context & Hooks. YouTube. https://www.youtube.com/watch?v=-40TBdSRk6E
* React Navigation. (n.d.). Nesting navigators. Retrieved October 25, 2024, from https://reactnavigation.org/docs/nesting-navigators/

</details>

<details>

  
<summary>How to deploy the flask app in pythonanywhere.com</summary>

## How to deploy the flask app in pythonanywhere.com

`pyhthonanywhere.com` helps to deploy different Python apps like Flask, and Django for free. We will be having some restriction like not able to change the url and will be having a data limit of 500mb. However, it works great.

1. Create a new account in pythonanywhere.com
2. Now we can see our dashboard and then go to the file section and create new folder that can be anything.
3. Now create a virtual environment inside the newly created folder. For that we have to go to the console tab and create a new bash console. Make sure we are inside the project directory and then run this command

   ```
   python -m venv venv
   ```
This will create a virtual environment inside the folder. I wish to share my understanding of about what is a python virtual environment

### What is a python virtual environment:

Imagine we are an artist with different projects. 
* Without vitual environment we will be having a big room with all the tools that can be used to any project.
* But with a virtual environment we will be having separate rooms for each projects having the necessary tools required for that project only. Like a little organized. 

So by creating a virtual environment to a project will be like creating a room for that project with only the necessary tools. This helps to avoid the package conflicts problems and do not commit that to the git hub as it might not work on the others and might be having security issues. 

Python Land. (n.d.). Python venv: How to create, activate, deactivate, and delete. Retrieved from https://python.land/virtual-environments/virtualenv

4. So now after creating we can activate the venv by the following command, note that the venv is the name that we given to our virtual environment that can be anything

```python
source venv/bin/activate
```
5. Create requirements.txt file, with all the required packages.

So in your computer, that is where we were running the flask app as local host we have run the following command in the flask app root directory

```python
pip freeze > requirements.txt
```

This will create a new requirements.txt file in the root directory and will list all the packages required for this project.

6. Remove the debug codes from your project:

    So in your computer before exporting the app.py file that is where we have all our apis we have to remove the code

   ```
   if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
   ```

   We were using this for the debug mode now we are switching to the production mode with do not need this it is a best practice for some security reasons.

7. Now in the pythonanywhere inside the our project folder that is in the files tab press the button `upload a file` and then upload the files `app.py` and the `requirements.txt` file  from your local machine.
8. Install the required packages to the virtual environment:
   ```python
   pip install -r requirements.txt
   ```
   So by the above command in the base we will be installing all of our necessary packages to our virtual environment.
9. Add the firebase configurations:
    So inside our project folder which has the app.py, requirements.txt, and the venv folder, we will create a new folder called `config` and inside the config folder upload the serviceAccountKey.json file from your computer that has the firebase configurations.
10. Create new web app:
    
     - Go to the web tab
     - Click `Add a new web app` Button
     - The create the web app by choosing the latest python version.
       
11. Update the WSGI file:

    Under the web app there is a link to modify the WSGI file:
    
    - Here change the path to the app folder. like `/home/perfectSky/mysite/venv` in my case as my user name is perfectSky
    - Change the virtual environment path. There will be a variable `VIRTUALENV = '/home/perfectSky/mysite/venv'`.

Thats all the setups just click save go back to the web tab, press reload and the our backend is live now.

</details>

<details>
  <summary>  How to keep the user information even after closing the application React Natvie </summary>

## How to keep the user information after sigin in or sigup in the local storage

So we are using Firebase Authentication persistence. This is the function allows users to remain authenticated even after closing and reopening the app. This means users don't need to log in again every time they use the application.

### Required Dependencies
```javascript
import { initializeAuth, getReactNativePersistence } from 'firebase/auth';
import AsyncStorage from '@react-native-async-storage/async-storage';
```

We need these two libraries that we can get from npm by the following command

```cmd
npm install firebase
npm install @react-native-async-storage/async-storage
```
Here the firebase auth have all the required packages related to the firebase so you don't have to add the `firebase/auth` package seprately.
### Basic Setup
```javascript
const auth = initializeAuth(app, {
    persistence: getReactNativePersistence(AsyncStorage),
});
```

## How It Works

1. **AsyncStorage Integration**
   - Firebase uses React Native's AsyncStorage to store authentication tokens locally on the device
   - These tokens are encrypted and securely stored
   - AsyncStorage is an asynchronous, persistent, key-value storage system

2. **Authentication Flow**
   - When a user logs in or signs up, Firebase creates an authentication token
   - This token is automatically stored in AsyncStorage
   - On app restart, Firebase checks AsyncStorage for valid authentication tokens
   - If a valid token exists, the user remains authenticated

3. **Token Management**
   - Firebase automatically handles token refresh
   - Expired tokens are automatically renewed when possible
   - Invalid tokens are cleared during logout

## Usage Example

```javascript
import { onAuthStateChanged } from 'firebase/auth';

// Listen for authentication state changes
onAuthStateChanged(auth, (user) => {
  if (user) {
    // User is signed in, redirect to home screen
    // The user object will be available even after app restart
    navigation.navigate('Home');
  } else {
    // No user is signed in, show login screen
    navigation.navigate('Login');
  }
});
```

## Best Practices

1. **Authentication State Management**
   - Always use `onAuthStateChanged` listener to detect authentication state
   - Don't rely on local state alone to track authentication status
   - Handle edge cases like token expiration

2. **Security Considerations**
   - Never store sensitive information in AsyncStorage directly
   - Let Firebase handle all token management
   - Implement proper logout functionality to clear stored tokens

3. **Error Handling**
   - Implement proper error handling for authentication state changes
   - Handle cases where persistence might fail
   - Provide fallback mechanisms for authentication failures

## Common Issues and Solutions

1. **Token Persistence Issues**
   - Ensure AsyncStorage permissions are properly set
   - Check if device storage isn't full
   - Verify AsyncStorage is properly linked in your React Native project

2. **Authentication State Syncing**
   - Use `onAuthStateChanged` instead of manual checks
   - Handle authentication state changes globally
   - Implement proper loading states while checking authentication

## Testing Persistence

To test if persistence is working correctly:

1. Log in to the application
2. Force close the application
3. Reopen the application
4. Verify that the user is still authenticated
5. Check if protected routes/screens are accessible
</details>
