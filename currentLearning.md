# Quiz — Lists & Review
### Date: 18.03.26

Answer each question below. Write your answers directly under each question.

---

**Q1.** What is the output of this code?

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4:2])
```

Your answer: 20 40

Correction: The values are right but it prints as a list — `[20, 40]`, not `20 40`.

---

**Q2.** What is wrong with this code?

```python
values = [5, 10, 15]
values = values.append(20)
print(values)
```

Your answer: values = values.append(20) would result in None being returned. I know from experience. It should just be values.append(20)

---

**Q3.** What is the difference between `pop()` and `remove()`? When would you use each?

Your answer: pop returns the value removed, remove does not. That is the only difference I know.

Correction: The bigger difference is how they target the item — `pop()` removes by **index**, `remove()` removes by **value**. Use `pop` when you know the position, `remove` when you know the value. The return behaviour is a secondary difference.

---

**Q4.** What does this print, and why?

```python
x = 10

def change():
    x = 99

change()
print(x)
```

Your answer: It prints 10, regardless of the function being called a local variable cannot change a global variable. 

---

**Q5.** Write a function called `is_passing` that takes a score and returns `True` if it's 50 or above, `False` otherwise. Write it in one line (no if/else).

Your answer: 

def is_passing(num):
    return num > 50

Correction: `>` fails for exactly 50. Should be `>=` — "50 or above" includes 50.

---

**Q6.** What does `//` do, and how is it different from `/`? Give an example.

Your answer: // rounds to the lowest whole number if it is a decimal. I.e. 7//2 is 3, whereas 7/2 is 3.5. % can be used also to count the remainder. 

---

**Q7.** Given this list:

```python
words = ["cat", "dog", "elephant", "fox", "ant"]
```

Write the code to print only the words longer than 3 characters, using a loop.

Your answer: 

for word in words:
    if len(word) > 3:
        print(word)

---

**Q8.** Explain in your own words: what does `enumerate()` give you that a normal `for` loop doesn't?

Your answer: enumerate also gives the index. I.e. 1 cat 2 dog, whereas a for loop would just give dog cat.

Correction: Enumerate starts at 0, not 1 — it would be `0 cat, 1 dog`.
