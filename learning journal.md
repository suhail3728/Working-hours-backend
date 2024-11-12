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
<summary>Firebase Authentication in React Native</summary>

## How to use Firebase Authentication in React Native

So If you have a Firebase app and if you are in the console tab:

1. On the left navigation you will see two tabs `Authentication` and Firestore database
2. Go to the authentication `Signin method` and click the `Add new provider`. Here you can choose any provider i have chosen the email and password my project.
3. Now change the configurations of the where you configured the Firebase database in your project.
 

```javascript
// Import required Firebase functions
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from 'firebase/firestore';

// Firebase configuration object
const firebaseConfig = {
  // Configuration details from Firebase console
  // (apiKey, authDomain, projectId, etc.)
  // Not shared due to security reasons
};

// Initialize Firebase services
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Initialize Auth with persistence
const auth = initializeAuth(app);
const analytics = getAnalytics(app);

// Export initialized services
export { app, auth, db }
```

This is how I changed my config file. The file is in `src/config/firebase.js` in the react native project folder.

```javascript
const auth = initializeAuth(app);
```
this is the important step, we import the auth package and wrap our app in Firebase auth.

Now our app is ready to do the authentication. The authentication happens in two places:

- sign in
- sign up

### Understanding Firebase Authentication

Firebase Authentication works by managing the entire authentication flow:
1. When users sign up or sign in, Firebase creates unique authentication tokens
2. These tokens are used to maintain user sessions
3. Firebase provides methods to track authentication state changes
4. It integrates well with other Firebase services like Firestore

The main components we use from Firebase Authentication are:
* `createUserWithEmailAndPassword`: For new user registration
* `signInWithEmailAndPassword`: For existing user login
* `onAuthStateChanged`: To listen to authentication state changes
* `auth`: The main authentication instance

### Setting up Firebase in the project

### How I implemented it in my project

#### 1. Setting up the Authentication Flow:

In my `App.js`, I implemented a structure that manages the authentication state:

```javascript
const App = () => {
  return (
    <AuthProvider>
      <Main />
    </AuthProvider>
  );
};

const Main = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const { setUserId } = useContext(AuthContext);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      if (user) {
        setUserId(user.uid);
        setIsAuthenticated(true);
      } else {
        setIsAuthenticated(false);
      }
      setIsLoading(false);
    });

    return unsubscribe;
  }, []);
}
```

#### 2. Implementing Sign In:

In my `SignInScreen.js`, I created a sign-in function using Firebase's authentication:

```javascript
const handleSignIn = async () => {
  try {
    setIsLoading(true);
    const userCredential = await signInWithEmailAndPassword(
      auth,
      email,
      password
    );
    setUserId(userCredential.user.uid);
  } catch (error) {
    setError('Invalid email or password');
  } finally {
    setIsLoading(false);
  }
};
```

#### 3. User Registration:

In `UserCreation4.js`, I implemented the sign-up functionality:

```javascript
const handleCreateUser = async () => {
  try {
    setLoading(true);
    const userCredential = await createUserWithEmailAndPassword(
      auth,
      email,
      password
    );
    const user = userCredential.user;
    setUserId(user.uid);
    
    // Create additional user data in database
    await createUser({
      userId: user.uid,
      name,
      business,
      mobileNumber,
      position: selectedPosition,
      address,
      businessType,
      numberOfEmployees: selectedNumOfEmployees
    });
  } catch (error) {
    Alert.alert('Error', error.message);
  } finally {
    setLoading(false);
  }
};
```

### What I learned:

1. **Firebase Setup:**
   - The importance of keeping Firebase configuration secure
   - How to properly initialize multiple Firebase services
   - Using persistence for better user experience

2. **Authentication State Management:**
   - Firebase's `onAuthStateChanged` is very useful for maintaining authentication state
   - It automatically handles token refreshing and validation
   - We can use it to switch between authenticated and non-authenticated views

3. **Error Handling:**
   - Firebase provides detailed error messages for authentication failures
   - It's important to handle loading states during authentication operations
   - Try-catch blocks are essential for managing authentication errors

4. **Context Integration:**
   - Using Context API with Firebase Authentication helps share user state across the app
   - It eliminates the need to pass user information through props
   - Makes it easier to access user information in deeply nested components

### Resources that helped me

* Firebase Documentation. (n.d.). Get Started with Firebase Authentication on Websites. Retrieved from https://firebase.google.com/docs/auth/web/start
* React Navigation. (n.d.). Authentication flows. Retrieved from https://reactnavigation.org/docs/auth-flow
* The Net Ninja. (2021). Firebase Auth in React Native. YouTube. https://www.youtube.com/watch?v=ql4J6SpLXZA
* Firebase Setup Guide. (n.d.). Adding Firebase to your React Native project. Retrieved from https://firebase.google.com/docs/react-native/setup

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

### How I used this in my project

#### 1. Wrap the firebase app like below while initializing the auth:

   ```javascript
   const auth = initializeAuth(app, {
    persistence: getReactNativePersistence(AsyncStorage),
  });
  ```

This is how I changed the config file in my project you can see the details in `src/config/firebase.js` file in React native project repository. 

```javascript
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { initializeAuth, getReactNativePersistence } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import AsyncStorage from '@react-native-async-storage/async-storage';

const firebaseConfig = {
  // our firbase config that we get from the firbase not sharing due to security reasons
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const auth = initializeAuth(app, {
    persistence: getReactNativePersistence(AsyncStorage),
  });
const analytics = getAnalytics(app);

export{app, auth, db}
});
```
So now when the the authentication happen the authentication token will be stored on the device locally. This is all the we need to do to make the user information stays even when the user closes the app. 

#### 2. Notify the firebase-auth when the authentication changes:

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

So here we are using the function `onAuthStateChanged` that will helps notifiy the `firebase-auth` when authentication changes that is at the time of login or signup and sigout. I have another documentation on explaining how authentication happens using firebase auth.
   


## In conclusion:

   - When a user logs in or signs up, Firebase creates an authentication token and inform firbase auth
   - This token is automatically stored in AsyncStorage
   - On app restart, Firebase checks AsyncStorage for valid authentication tokens
   - If a valid token exists, the user remains authenticated
   - If the user sign out remove the authentication token and inform firebase auth
   - 
## Resources that helped me 


- Firebase. Authentication State Persistence. Retrieved November 11, 2024, from https://firebase.google.com/docs/auth/web/auth-state-persistence

- Adrian Twarog.(2020) AsynStorage React-native | AsyncStorage Tutorial. YouTube. https://youtu.be/2Oz-OLB8FQQ

- Jorge Vergara. (2021). Understanding the firebae auth persistence. YouTube. https://youtu.be/PRGHWgTydyQ](https://www.youtube.com/watch?v=si5fhwYVakk



