# Lockme
A simple PoC of ransomeware developed in python3



![Screenshot](https://img.shields.io/badge/Platform-Windows-brightgreen)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python%203-blue)
![Screenshot](https://img.shields.io/badge/Language-Php-blue)




## How does Lockme work? 🚀



Lockme scans the files in a previously defined directory or several, and encrypts them with Fernet, when it finishes encrypting the files, it encrypts the Fernet key with a public key of RSA-4096 and sends it to a server along with the ID of the victim.

After this process, the victim of Lockme will get a GUI to decrypt his files



### Requirements 📋



* An RSA key pair
* A web server where to receive the keys
* Python3



### How use it? 🔧



_You have to modify the following variables with your options__
```
13. server
14. serverrsa
15. directories
```


### Using Pyinstaller to get a exe 🛠️



To avoid errors when using pyinstaller change the boolean variable ```iamexe``` to true.



### Disclaimer ⚠️



** As I have already mentioned before, this tool is a PoC, I do not misuse that it can be given **



### Authors ✒️

* s4tak

//Regards
