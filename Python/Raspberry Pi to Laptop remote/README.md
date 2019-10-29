This project was created as my first proper project with a Raspberry Pi and to introduce me to using different boards
and components with a Raspberry Pi. The code for this project is set into two different sections, one lot of code is for the server or the device you want to control remotely and the second runs on the Pi to control your chosen device. 

Server code.

Using a combination of Pythons "sockets" and "pyautogui" libraries I was able to write a small script that opens up a socket connection for the client device to connect to which then waits to receive a connection before processing any data it receives. During previous experiments with sockets I also learnt to make things easier for myself whenever I open up a connection by including the ""






Client code.



Compiling the code into an executable file.
