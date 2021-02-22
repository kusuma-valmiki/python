1. abs()
The abs() is one of the most popular Python built-in functions, which returns the absolute value of a number.

A negative value’s absolute is that value is positive.

>>> abs(-7)
Output

7
>>> abs(7)
Output

7
>>> abs(0)
2. all()
The all() function takes a container as an argument. This Built in Functions returns True if all values in a python iterable have a Boolean value of True.

An empty value has a Boolean value of False.


>>> all({'*','',''})
Output

False
>>> all([' ',' ',' '])
Output

True
3. any()
Like all(), it takes one argument and returns True if, even one value in the iterable has a Boolean value of True.

>>> any((1,0,0))
Output

True
>>> any((0,0,0))
Output

False
4.  ascii()
It is important Python built-in functions, returns a printable representation of a python object (like a string or a Python list).

Let’s take a Romanian character.


>>> ascii('ș')
Output

“‘\\u0219′”
Since this was a non-ASCII character in python, the interpreter added a backslash (\) and escaped it using another backslash.

>>> ascii('ușor')
Output

“‘u\\u0219or'”
Let’s apply it to a list.

>>> ascii(['s','ș'])
Output

“[‘s’, ‘\\u0219’]”
5. bin()
bin() converts an integer to a binary string. We have seen this and other functions in our article on Python Numbers.

>>> bin(7)
Output

‘0b111’
We can’t apply it on floats, though.

>>> bin(7.0)
Output

Traceback (most recent call last):File “<pyshell#20>”, line 1, in <module>

bin(7.0)

TypeError: ‘float’ object cannot be interpreted as an integer

6. bool()
bool() converts a value to Boolean.

>>> bool(0.5)
Output

True
>>> bool('')
Output

False
>>> bool(True)
Output

True

7. bytearray()
bytearray() returns a python array of a given byte size.

>>> a=bytearray(4)
>>> a
Output

bytearray(b’\x00\x00\x00\x00′)

>>> a.append(1)
>>> a
Output


bytearray(b’\x00\x00\x00\x00\x01′)

>>> a[0]=1
>>> a
Output

bytearray(b’\x01\x00\x00\x00\x01′)

>>> a[0]
Output

1

Let’s do this on a list.

>>> bytearray([1,2,3,4])
Output

bytearray(b’\x01\x02\x03\x04′)

8. bytes()
bytes() returns an immutable bytes object.

>>> bytes(5)
Output

b’\x00\x00\x00\x00\x00′

>>> bytes([1,2,3,4,5])
Output

b’\x01\x02\x03\x04\x05′

>>> bytes('hello','utf-8')
Output

b’hello’Here, utf-8 is the encoding.

Both bytes() and bytearray() deal with raw data, but bytearray() is mutable, while bytes() is immutable.

>>> a=bytes([1,2,3,4,5])
>>> a
Output

b’\x01\x02\x03\x04\x05′

>>> a[4]=
Output

3Traceback (most recent call last):

File “<pyshell#46>”, line 1, in <module>

a[4]=3

TypeError: ‘bytes’ object does not support item assignment

Let’s try this on bytearray().

>>> a=bytearray([1,2,3,4,5])
>>> a
Output

bytearray(b’\x01\x02\x03\x04\x05′)

>>> a[4]=3
>>> a
Output

bytearray(b’\x01\x02\x03\x04\x03′)

9. callable()
callable() tells us if an object can be called.

>>> callable([1,2,3])
Output

False

>>> callable(callable)
Output


True

>>> callable(False)
Output

False

>>> callable(list)
Output

True

A function is callable, a list is not. Even the callable() python Built In function is callable.

10. chr()
chr() Built In function returns the character in python for an ASCII value.

>>> chr(65)
Output

‘A’

>>> chr(97)
Output

‘a’

>>> chr(9)
Output

‘\t’

>>> chr(48)
Output

‘0’

11. classmethod()
classmethod() returns a class method for a given method.

>>> class fruit:
                def sayhi(self):
                                print("Hi, I'm a fruit") 
       
>>> fruit.sayhi=classmethod(fruit.sayhi)
>>> fruit.sayhi()
Output

Hi, I’m a fruit

When we pass the method sayhi() as an argument to classmethod(), it converts it into a python class method one that belongs to the class.

Then, we call it like we would call any static method in python without an object.

12. compile()
compile() returns a Python code object. We use Python in built function to convert a string code into object code.

>>> exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
Output

12
Here, ‘exec’ is the mode. The parameter before that is the filename for the file form which the code is read.


Finally, we execute it using exec().

13. complex()
complex() function creates a complex number. We have seen this is our article on Python Numbers.

>>> complex(3