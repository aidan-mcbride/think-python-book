# 14: Files (Data Persistence)

## `14.1` Persistence

[**Persistence**](https://en.wikipedia.org/wiki/Persistence_%28computer_science%29) - State/data that outlives the process that created it. Persistent data is stored in permanent storage, such as a hard drive.

## `14.2` Reading and Writing

Files can be written by opening them in write mode and using the `write` method:

```python
fout = open('output.txt', 'w')	# fout means file output
fout.write(some_data)
# returns number of characters written to file
fout.close()
```

* Write mode will create the given file if it doesn't exist
* Write mode will erase all existing data in the file.

## `14.3` Format Operator

**Format Operator `%` :** insert data into a string.

```python
apples = 43
"There are %d apples" % apples	# %d means format as decimal integer
# 'There are 43 apples'
```

Alternatively, you can use the [**string format method**](https://docs.python.org/3/library/stdtypes.html#str.format):

```python
apples = 43
"There are {} apples".format(apples)
# 'There are 43 apples'
```

## `14.4` Filenames and Paths

files are organized in *directories*. The directory that a program is being run from is the *current directory*.

```python
import os
current_dir = os.getcwd()
```

A **path** identifies a file or directory. **Relative paths** are paths relative to the *current directory*. Paths that begin with **`/`** are **absolute paths**.

## `14.5` Catching Exceptions

**`try`** and **`except`** can be used for *catching* exceptions:

* Python will attempt to run code within the `try` block.
* If an exception is raised, python will execute the code within the `except` block.

## `14.6` Databases

**Database** - a file that stores organized data.

Python's [**`dbm`**](https://docs.python.org/3.7/library/dbm.html) module provides an interface for working with unix 'database' files*(quotes from python docs - I sense that these aren't real databases)*.

```python
import dbm
my_db = dbm.open('database-file', 'c') # 'c' means create if doesn't exist
```

## `14.7` Pickling

`dbm` requires that keys and values are either strings or bytes. Python's [**`pickle`**](https://docs.python.org/3/library/pickle.html) module can be used for converting data to and from dbm-compatible types.

```python
import pickle
pickle.dumps(data)	# converts data to pickle string
pickle.loads(data)	# converts pickle string to data
```

## `14.9` Writing Modules

Any file containing python code can be imported as a module.

Modules often use the following bit of code:

```python
if __name__ == '__main__':
    # do whatever
```

`__name__` is a built-in variable that is assigned when the program runs. If the program is running as a script, `__name__` has the value `__main__`; if the program is being imported as a module this is not the case.

## `14.10` Debugging

The built-in function `repr` takes an object and returns a string representation of that object.

---

## *`14.12` Exercises*

### `Exercise 14.1`

> Write a function called `sed` that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
>
> If an error occurs while opening, reading, writing, or closing files, your program should catch the exception, print an error message, and exit.

```python
# exercises/14.1.py

def sed(filename1, filename2, pattern='', replace=''):
    """
    filename1:  file to copy from
    filename2:  file to copy to
    pattern:    string to be replaced
    replace:    string to replace pattern with
    """
    # see here for text IO methods:
    # https://docs.python.org/3.7/library/io.html#io.TextIOBase.read
    try:
        fin = open(filename1, 'r').read().replace(pattern, replace)
        fout = open(filename2, 'w')
        fout.write(fin)
    except:
        print("Error occurred while copying file")

```

### `Exercise 14.2`

> Write a module that imports `anagram_sets` and provides two new functions: `store_anagrams` should store the anagram dictionary in a "shelf"; `read_anagrams` should look up a word and return a list of its anagrams.

*A [**'`shelf`'**](https://docs.python.org/3/library/shelve.html) is a way to persist dictionary data.*

```python
# exercises/14.2.py

import os, shelve

import anagram_sets

def store_anagrams(filepath):
    """
    creates dictionary of anagrams in a list of words
    in a given file at filepath
    stores dictionary in a 'shelf'
    """
    # extract filename from given path
    # for use as shelf file name
    filename = os.path.splitext(filepath)[0]
    anagrams = anagram_sets.all_anagrams(filepath)
    print(anagrams)
    try:
        with shelve.open(filename) as db:
            for key, value in anagrams.items():
                db[key] = value
    except:
        print('error writing to shelf')

def read_anagrams(database, word):
    """
    looks up a given word in a given database
    returns a list of of anagrams for that word
    """
    try:
        with shelve.open(database) as db:
            return db[word]
    except:
        print('error reading from shelf')


# run program
if __name__ == '__main__':
    store_anagrams('exercises/test.txt')
    print(read_anagrams('exercises/test', 'glo'))

```

### `Exercise 14.3`

> In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.

1. > Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix(like `.mp3`).

   ```python
   # exercises/14.3.1.py
   
   import os
   
   def walk(dir, ext=None):
       """
       walks through a given directory and all subdirs
       returns the abspath for any files with the given extension
       if no ext given, returns all files
       """
       for root, dirs, files in os.walk(dir):
           for file in files:
               if ext == None or os.path.splitext(file)[1] == ext:
                   print(os.path.abspath(file))
   
   if __name__=="__main__":
       walk('.', '.txt')
   
   ```

   