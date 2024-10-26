
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

So I figured that out with the help of nested navigations from this article https://reactnavigation.org/docs/nesting-navigators/. by using the tab navigator as a component inside the stack navigator. 





## 26rd September 

So I learned how to navigate between screens in react-native, I searched a little bit about the type script, functional components,  while I was trying to understand why using jsx file instead of js and typescript is the super set of javascript where you can create your own type actually that is what I am using in the navigation too. Then I created how to create dynamic components like button in react native and passing the values as props. 




   
