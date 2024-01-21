My approach to this project is utilizing the built-in socket, ssl, and JSON libraries to 
create a secure connection between the client and server. These libraries allow me to implement 
easily the functionality of the project.  

As for the guessing logic, I simply utilized the conditions of 1 and 2 in the marks to filter out 
the word lists progressively, which is very straightforward. If there is a 1 in the marks, 
then I filtered out every word without the letter in that position and without that letter. 
If there is a 2 in the marks, I only kept the words that have the letter in that position.
I tested and troubleshooted the programs by printing out and examined the received messages from the server until 
I received the two correct secret flags.

To follow the requirements of the project with python script.
I added shebang line at the top of the script to indicate the interpreter to use.  

```python
#!/usr/bin/env python3
```

And I made the script executable by running the following command in the terminal.

```bash
chmod +x client.py
```

Then I rename the file as `client`

```bash
mv client.py client
```

So that I can run the script by:

```bash
$ ./client <-p port> <-s> <hostname> <Northeastern-username>
```
