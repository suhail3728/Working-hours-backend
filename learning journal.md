
# Learning journal 
## Using React native use context. 

useContext is a react native hook that helps with access the value of a parameter from any screen under this context without manually passing from each components. 

### react native hooks 
Hooks are special functions in the react that helps in manage the states in different componets. Like useState hook , helps to change the variable state. useEffect hooks the functions will be called when the screen is loaded or when the value of variable is changed. 

While useing useEffect(()=> randomFunctions(); {},[]); the codes in the the use effects runs the when the component loads. And if we are any variable inside the square bracket then the functions called inside the useEffect changes when the value of the variable changes like  useEffect(()=> randomFunctions(); {},[userId]); , the codes inside the useEffect will be called whenever the value of the userId is changed.

These hooks can only be called inside a functional component in react. So a functional component is any javascript function that return jsx. Jsx is certain syntax of javascript where we create html like structues.

These hooks are very useful in my project, I use the useState to assign values to the variable. useEffects are used to show the ui according to the respective users. And the useContext was the one that helped me to pass parameters between different type of Stacks in my project.

### How it was useful in my project. 

So in react navigation happens by creating a navigation container that we can import from the package react-navigation and By creating Stack , where Stack is a createStackNavigator function we can import from react navigation. So we can create different Stack.Navigator inside the navigation container. And inside the Stack.Navigators we can use our screens by using Stack.screen.

So in my case I have two different types of stacks one is the AuthStack which have the screeens for user login or sign up and that is a Stack.Navigator and the other one is the userStack which contain the screens that the user will be using after authentication and that is a Tab.navigator where tab is a createBottomTabNavigator function that we import from @react-navigation/bottom-tabs. So I was troubling with moving how to move from the Stack navigator to the Tab navigator.

So I figured that out with the help of nested navigations from this article https://reactnavigation.org/docs/nesting-navigators/. by using the tab navigator as a component inside the stack navigator. And the next challege was how to pass the user id after authentication from the auth stack to userStack. Here evethough i am using the my bottoms tabs in userStack inside a stack navigator component, both are different files and different stacks. So I was struggling to find a way and then I found the useContex hook.

### How to use the useContext hook. 
![Screenshot 2024-10-25 211559](https://github.com/suhail3728/Working-hours-backend/blob/main/Screenshot%202024-10-25%20211559.png)

So I first created a new file call AuthContext and we are exportinig two things from this file AuthContext and AuthProvider, these are the names give by me this can be any names. Here Auth context is the createContext function that the we import from react and AuthProvider is a functional component accepting a childern parameter. So I declared the userId and the setUser Id inside the AuthProvider and then the AuthProvider functional component is returning an AuthContext.provider where you can define the values that the childern of this can be used, in my case i have the userId and the setUser function inside the value so that any of the children element can use these. 

Then after creating the AuthContext file, I wrapped my Navigation container in the App.js file with the AuthProvider and then I imported the setUserId function in the usercreation page in the AuthStack and set the value for the userId and then when I move to the userStack I import the userId from the AuthContext and userthe userId. This is possible because as we wrapped our main navigator inside the Authprovider and we can set or use the userId value from any screens inside the children of the AuthProvider, this was very useful. 


### Resources that helped me : 

* Crawford, T. (2023, September 22). React Navigation - Nesting Navigators. YouTube. https://www.youtube.com/watch?v=6RhOzQciVwI
* NetNinja (2020). React Context & Hooks. YouTube. https://www.youtube.com/watch?v=-40TBdSRk6E
* React Navigation. (n.d.). Nesting navigators. Retrieved October 25, 2024, from https://reactnavigation.org/docs/nesting-navigators/







   
