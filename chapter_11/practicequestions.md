1. Write an assert statement that triggers an AssertionError if the variable 
spam is an integer less than 10.  
Answer: assert spam >= 10, 'Spam is less than 10.'

2. Write an assert statement that triggers an AssertionError if the variables 
eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).  
Answer: assert eggs.lower() != bacon.lower(), 'eggs and bacon are the same.'

3. Write an assert statement that always triggers an AssertionError.  
Answer: assert False, 'This assert statement always triggers.'

4. What are the two lines that your program must have in order to be able to 
call logging.debug()?  
Answer: import logging and a logging.basicConfig() statement (e.g., logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')).

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?  
Answer: import logging and a logging.basicConfig() statement with a filename 
parameter (e.g., logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')).

6. What are the five logging levels?  
Answer: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

7. What line of code can you add to disable all logging messages in your 
program?  
Answer: A logging.disable() statement (e.g., logging.disable(logging.DEBUG)).

8. Why is using logging messages better than using print() to display the same message?  
Answer: You can easily toggle on/off logging messages from appearing on the
console, add timestamps to your messages, and save logging message to a file.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?  
Answer: Step In executes the next line of code and then pauses. If the next line of code is a function call, the debugger will 'step into' the function and execute the first line of code.  
Step Over is the same thing as Step In, but if 
the next line of code is a function call, Step Over will execute the function at full speed and pause at the fucntion call's end (Step Over is great if you don't care about the code inside a function).  
Step Out executes code at full speed in a function until the function ends. If you entered a function using Step In and now you want to exit out of it, use Step Out.

10. After you click Continue, when will the debugger stop?  
Answer: Program executes normally until it terminates or reaches a breakpoint.

11. What is a breakpoint?  
Answer: Makes the debugger pause whenever the program execution reaches a specific line.

12. How do you set a breakpoint on a line of code in Mu?  
Answer: In Mu, click the line number on the lefthand side of the program.