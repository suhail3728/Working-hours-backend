# Reflections on skills learned from DGL Courses

<details>
  <summary> Effective use of javascript techniques</summary>

## Effective use of javascript techniques

So I was a student in the course `DGL 113 CVS1 2024 Winter Term`

That course was really helpful it was taught by Frank Lu, He taught CPS-100 too, that was my first computer science course ever and I am always grateful for helping me build my undertandings and giving me a good foundation on programming techniques.
Now, during the course `DGL 113` I learned a lot of javascript techniques one of them is the use of `setTimeOut` funciton. This function helped me to solve on of the major issue in my project. I will explain how this function helped me, first let me give a brief description about this function

### setTimeOut function:

So this is a javaScript buit-in function that is used to delay an action for a given time.

```javascript
setTimeout(() => {
  setIsAuthenticated(true);
}, 1000);
```

This is an example how I used the function in my project. Here there are two things we have to focus on:

- First, the action that has to be delayed in this case that is `setIsAuthenticated(true)`
- Second, how much time do we have to delay, here that is `1000`. Note that this is 1000 milli seconds milli means 1/1000. so here its 1000 milli seconds that is 1s.

#### How this function helped me in my project

So was struggling with an issue in my project

### Problem:

So while creating a new user, we navigate to the home page but the home page does'nt have the created user information. I will explain this in a simple step by step

1. Below is a simple demonstration of the function that create new user, the full version of the code is in `src/screens/EmployeeCreate.js`

```javascript
const handleCreateUser = async () => {
  const userCredential = await createUserWithEmailAndPassword(
    auth,
    email,
    password
  );
  const user = userCredential.user;
  await createUser(userData);
};
```

- The function `createUserWithEmailAndPassword()` is provided by firebase-auth package. This create a user in firebase authentication and create an authentication token
- The function `createUser()` is an api calling function defined by me in for calling the api in `src/service/api.js` file.

2.  Below is a simple version of my home screen that switch the navigation based on the users authentication state.

```javascript


const Main = () => {
const [isAuthenticated, setIsAuthenticated] = useState(null);

onAuthStateChanged(auth, async user => {
if (user) {
setIsAuthenticated(true);
} else {
setIsAuthenticated(false);
}
});
return (
<NavigationContainer>
{isAuthenticated ? <UserStack /> : <AuthStack />}
</NavigationContainer>
);
};

```
 - The function `onAuthStateChanged()` is a function provided by the firebase-auth which get the state of the user whether authenticated or not.This function will get the user token immideattly after creating from the page usercreation page using the function `createUserWithEmailAndPassword()` as mentioned before.
 - `isAuthenticated` is a boolean that becomes true when authentication happens.
 - When the `isAuthenticated` is true it we go to the `UserStack` according to the logic ` {isAuthenticated ? <UserStack /> : <AuthStack />}`

#### Reason for the problem:
* So the problem is user go to the `HomeScreen` that is in the `UserStack` right away after the authentication.
* The api function `createUser(userData);`  takes atleast one second to create the date in the firebase database. But we are going to the home page before creating the data in the database 

* In the home page first thing that we do is do an api call to get the user detail using `useEffects`. 

* So we are trying to get the user information in the homepage before creating the user in formation in the database.


### Solution

```javascript


const Main = () => {
const [isAuthenticated, setIsAuthenticated] = useState(null);

onAuthStateChanged(auth, async user => {
if (user) {
setTimeout(() => {
  setIsAuthenticated(true);
}, 1000);
} else {
setIsAuthenticated(false);
}
});
return (
<NavigationContainer>
{isAuthenticated ? <UserStack /> : <AuthStack />}
</NavigationContainer>
);
};

```

* There is only one change in the App.js file that is we wrap the `setIsAuthenticated(true)` with a `setTimeOut` function and delay the action for a second.

* With this one second delay we navigate to the `HomeScreen` after one second of validation.

* This one second is enough for the api call `createUser()` to create the user data in the firebase database. 

* And now when we try to get user data in the `HomeScreen` we get the user because its already create a second ago. 

This is how we see the user information properly after creating a user in this case.



#### In conlusion

This is just one instance where learning the javaScript helped me to solve an issue in my project. Moreover, this project's fronend is build in `React Native`, which is a javascript framework. So with a good understanding of the javascript it was helpful for me to learn this frame work for the project.

</details>


