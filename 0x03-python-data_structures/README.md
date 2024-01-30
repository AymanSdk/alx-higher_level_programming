# Python Data Structures: Lists and Tuples
[![PyCodeStyle](https://img.shields.io/badge/code%20style-pep8-brightgreen.svg)](https://github.com/PyCQA/pycodestyle)

This README provides an overview of two fundamental data structures in Python: Lists and Tuples. These data structures are essential for organizing and manipulating collections of data in Python. Understanding how to use lists and tuples effectively is crucial for any Python programmer.

## Table of Contents
- [Lists](#lists)
  - [Creating Lists](#creating-lists)
  - [Accessing Elements](#accessing-elements)
  - [Modifying Lists](#modifying-lists)
  - [Common List Methods](#common-list-methods)
- [Tuples](#tuples)
  - [Creating Tuples](#creating-tuples)
  - [Accessing Tuple Elements](#accessing-tuple-elements)
  - [Immutable Nature of Tuples](#immutable-nature-of-tuples)
  - [Common Tuple Operations](#common-tuple-operations)
- [Conclusion](#conclusion)

---

## Lists

Lists are one of the most versatile and commonly used data structures in Python. They are ordered collections of items, and each item can be of any data type. Lists are defined by square brackets `[]`, with elements separated by commas.

### Creating Lists

To create a list, enclose your elements within square brackets:

```python
my_list = [1, 2, 3, 'Python', 'List']
```

### Accessing Elements

You can access elements in a list using indexing. Python uses zero-based indexing, meaning the first element is at index 0.

```python
first_element = my_list[0]  # Access the first element
last_element = my_list[-1]  # Access the last element
```

### Modifying Lists

Lists are mutable, which means you can change their contents after creation. You can add, remove, or modify elements.

```python
my_list.append(4)           # Add an element to the end
my_list[2] = 'New Value'    # Modify an element
my_list.remove('Python')    # Remove an element by value
del my_list[1]              # Remove an element by index
```

### Common List Methods

Python provides several built-in methods for working with lists:

- `append()`: Add an element to the end of the list.
- `insert()`: Insert an element at a specific index.
- `remove()`: Remove the first occurrence of an element by value.
- `pop()`: Remove and return an element by index.
- `sort()`: Sort the list in ascending order.
- `reverse()`: Reverse the order of elements.
- `len()`: Get the length of the list.
- `count()`: Count the number of occurrences of an element.
- `index()`: Find the index of the first occurrence of an element.

## Tuples

Tuples are similar to lists but with one crucial difference: they are immutable. Once you create a tuple, you cannot change its elements. Tuples are defined by parentheses `()`.

### Creating Tuples

To create a tuple, enclose your elements within parentheses:

```python
my_tuple = (1, 2, 3, 'Python', 'Tuple')
```

### Accessing Tuple Elements

You can access tuple elements using indexing, just like with lists. Tuple indexing is also zero-based.

```python
first_element = my_tuple[0]  # Access the first element
last_element = my_tuple[-1]  # Access the last element
```

### Immutable Nature of Tuples

The immutability of tuples means you cannot add, remove, or modify elements once a tuple is created. This immutability provides data integrity and makes tuples suitable for situations where you want to ensure the data remains unchanged.

### Common Tuple Operations

Although you cannot change a tuple's content, you can perform various operations on tuples, such as concatenation and repetition:

```python
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2  # Concatenation
repeated_tuple = tuple1 * 3          # Repetition
```
