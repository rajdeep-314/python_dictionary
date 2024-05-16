## Dictionaries

I'm attempting to program my own version of Python's dictionaries using Python
<br><br>
I have implemented hash tables, and the techniques I use for handling hash collisions, or hash table resizing are extremely similar to those internally employed in Python's dictionaries, if not the same. <br>
For handling collisions, I use linear probing. <br>
During a hash table resizing, all hashes are re-evaluated.
<br><br>
Currenttly, the delete functionality is very primitive. A new dictionary with all key-value pairs except those with the deleted key is created, which is time consuming and inefficient. <br>
I plan to incorporate the approach that Python uses, by assigning dummy values to the empty slots. This will lead to some major changes in the rest of the code.
<br><br>
The comments associated with the various methods describe the functionality of the methods pretty well.
<br><br>
As an iterable can be passed as an argument for constructing these dictionaries, one can use generators as well. <br>
<br>
For example, try this out :
<br>
```python
x = dictionary((chr(i+64), i) for i in range(1, 11))
print("The dictionary is :")
x.print()
print("\nLength =", x.get_length())
print("\nCorresponding hash table :")
x.show_hash_table()
```
