Title:Understanding Event Loop in Python
Date: 2021-12-03 10:20
Modified: 2021-12-05 19:30
Category: JavaScript
Tags: programming, event
Slug: event-loop
Authors: Fitri Rahim
Summary: Short version for index and feeds
Self: hello

Event loop is the important component of the asyncrhronoous concept in Python. To understand how the async work in Python we first need to look at event loop which is the heart of the async concept.

You can imagine the event loop just as a big while loop continously checking the input and output and take in the input when available then proceed looping if there's no output available at the time it will skip until the output is ready then it will output the result.

## Understanding the sequences

Lets try to visualize this with the sequences below:

- Event loop start
- checking for input
- checking for output
- checking for input
- Input available take it and sent for processing
- checking for output
- checking for input
- checking for output
- checking for input
- Input I2 available - sent for processing
- checking for output
- Output O2 available - sent for display
- checking for input
- checking for output 
- Output I1 available - sent for display
- continues loop until stop

From the above we can see, even the input I1 was taken first, but since the processing still ongoing, it will not wait for the I1 to return the result, instead it will continue looping for input and output until it got I2 which sent for processing and ready earlier than I1, thus the result was return immedietly before the I1, and only when I1 finished processing it return the result.


The input processing can be anything, either sleep, accessing disk, database, or even http requests. 

In case of HTTP requests, the loop will not wait for the requests to process first before taking another requests, it will continue taking requests after request and only return the result when the processing finish. Of course all these happening real fast as Python executing.

This is why it was called as non-blocking IO process, the output for the previous request will not hinder the new request made to the program.
