<h1>TASK 1</h1>
<h2>Exercise:</h2>
You need to develop a program that simulates the reception and processing of requests. The program should automatically generate new requests (identified by a unique number or other data), add them to a queue, and then sequentially remove them from the queue for “processing,” thereby simulating the operation of a service center.

Here is pseudocode for the task using a queue (`Queue` from Python’s `queue` module) for a request processing system:
```
import Queue

Create a request queue
queue = Queue()

Function generate_request():
    Create a new request
    Add the request to the queue

Function process_request():
    If the queue is not empty:
        Remove a request from the queue
        Process the request
    Else:
        Display a message that the queue is empty

Main program loop:
    While the user has not exited the program:
        Execute generate_request() to create new requests
        Execute process_request() to process requests
```
In this pseudocode, two main functions are used: `generate_request()`, which generates new requests and adds them to the queue, and `process_request()`, which processes requests by removing them from the queue. The main loop of the program executes these functions, simulating a continuous flow of incoming requests and their processing.

<h2>Solution</h2>
See file: <b>task_01.py</b>


<h1>TASK 2</h1>
<h2>Exercise:</h2>

You need to develop a function that takes a string as an input parameter, adds all its characters to a double-ended queue (deque from Python’s `collections` module), and then compares characters from both ends of the queue to determine whether the string is a palindrome. The program should correctly handle both even- and odd-length strings, and it should be case-insensitive and ignore spaces.

The code is implemented using a deque from Python’s `collections` module.

The program checks whether a given string is a palindrome, taking into account both even and odd numbers of characters, and is insensitive to case and spaces.

<h2>Solution</h2>
See file: <b>task_02.py</b>
