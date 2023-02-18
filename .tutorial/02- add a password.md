# Add a password

### Let's add a bit more input.

👉 Now that we have input for both a username and password, we need to change our `if` and `elif` statements just a bit so both the username **and** password must match for Mark and Suzanne to login.
```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
```



&nbsp;

👉 In the code below the username and password must **both** be correct for Mark to login. 

 ```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
```

&nbsp;

👉 Suzanne's password is 'Su74nne'. Can you add that to the code above? (HINT: It should be *very* similar to Mark.)



<details><summary> Answer 👀 </summary>
  
 ```python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
```

</details>

