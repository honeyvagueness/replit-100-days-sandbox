# What the elif is this? 
- The `elif` command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many `elif` statements as you want, but they **must** go in between `if` and `else` and have the same indentation.
  The `print` statements in your `elif` command need to line up with the indent of the other `print` statements.

&nbsp;

Where would an `elif` statement go in the code below?

```python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
  ```

<details> <summary> Answer 👀</summary>

- An `elif` statement would go in between the `if` and `else` statements.
</details>

&nbsp;

👉 Add this `elif` statement to the code above. Make sure you indent properly AND put it in **between** the if and else statements!

```
elif username == "suzanne":
  print("Hey there Suzanne!")
```
&nbsp;

Your code should look like this: 

<details> <summary> Answer 👀</summary>
  
```python
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")

  ```
</details>

### How easy was that? You will be a pro in no time!


