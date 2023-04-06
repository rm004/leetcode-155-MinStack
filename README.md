LeetCode Prompt:

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
  
Solution:
    
    This problem can be tricky at first if this is your first time encountering one like this. LeetCode rates this a Medium problem, however, the solution
    is fairly simple. I decided to implement my Stack data structure using a List. I also created a variable to hold the current top of the Stack's index. 
    The push(), pop(), and top() functions all can easily be made to run in O(1) time complexity just by making them like you would any other Stack. The 
    crux of this problem is the getMin() function because that also needs to run in O(1) time. The trick is to use an additional Stack to keep a list of 
    the minimum elements as you add them to the main Stack. I called this second Stack minStack and again implemented it using a List. This will require 
    some modification of the push() and pop() functions from a regular Stack. First, whenever you call the push() function you add the new value to the top
    of the main Stack as you would any other time. However, you then check to see if the value you just added to the top of the main Stack is less than or 
    equal to the current top of minStack which is the current min value of the main Stack. If it is then you push the new value onto the minStack and end 
    your push() function. Moving to the pop() function, before you pop the value at the top of the main Stack you first have to check whether that value is
    the current min value of the main Stack or in other words the top value of the minStack. If it is then you must first pop that value off the top of 
    the minStack because once you remove it from the main Stack then it will no longer be the min value of the main Stack. After you check that condition, 
    you then can pop the top value off the main Stack as you would normally. Now you can run your getMin() function in O(1) time complexity while keeping 
    the other function the same O(1) time complexity simply by returning the top of the minStack when getMin() is called.
