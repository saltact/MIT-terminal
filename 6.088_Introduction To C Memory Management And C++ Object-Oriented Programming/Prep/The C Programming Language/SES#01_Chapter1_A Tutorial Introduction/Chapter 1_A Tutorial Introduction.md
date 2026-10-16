> - *14:00 - Wednesday Oct 14th, 2026*
> - [Google Calendar](calendar.google.com)

# Introduction
---
## A. Origin of C
- C is a general-purpose programming language and it has been closely associated with the [UNIX system](https://www.geeksforgeeks.org/linux-unix/introduction-to-unix-system/)
- Useful for ***writing compilers and operating systems***, it has been used equally well to write major programs in many different domains.
* The C's important concepts stem from the language [BCPL](https://www.cl.cam.ac.uk/~mr10/BCPL.html) and the BCPL on C proceeded indirectly through the language B, which was written by Ken Thompson in 1970 for the first UNIX system on the [DEC PDP-7]()
## B. Fundamental overview of C
- BCPL and B are "typeless" language.
-  C provides a variety of **data types**. The fundamental types are *characters*, and *integers* and *floating-point numbers of several sizes*.
- **Hierarchy of derived data types** created with *pointers, arrays, structures, and unions.*

* **Expressions** are formed from operators and operands; any expression, including an assignment or a function call, can be a **statement**.

- **Pointers** provide for machine-independent address arithmetic

## C. Control-flow overview in C
- Control-flow constructions including statement grouping, decision making (`if-else`), *selecting one of a set of possible cases* (`switch`), looping with the termination test at the top (`while, for`) or at the bottom (`do while`), and early loop exit (`break`).
## D. Function overview in C
- Functions may return values of basic types, structures, unions, or pointers.
- May be called *recursively*.
- Local variables are typically "automatic", or created [anew](https://dictionary.cambridge.org/dictionary/english/anew) with each invocation.

* Function definitions may not be nested but variables may be declared in a block-structure fashion.
* Also, the functions of a C program may exist in separate source files that are compiled separately.
* Variables may be internal to a function, external but known only within a single source file, or visible to the entire program.

## E. Overview characteristic of C.
- A pre-proccessing step performs macro substitution on program text, inclusion of other source files, and conditional compilation.
- C is relatively "low level" language though it is not [pejorative](https://dictionary.cambridge.org/dictionary/english/pejorative); it simply means that C deals with the same sort of objects that most computers do, namely ***characters, numbers and addresses***. These maybe combined and moved about with the *arithmetic* and *logical* operators implemented by real machines.

## F. Overview of objects and data structures in C
- Have no operations do deal directly into composite objects and data structures such as character strings, sets, lists, or arrays. Since the language does not define any ***storage allocation facility*** other than `static` definition and the ***stack discipline*** provided by the local variables of functions; there is no `heap` or **garbage collection.**
- C itself provides no input/ output facilities; there are no `READ` and `WRITE` statements, and no built-in file access methods. --> All of these high-level mechanisms must be provided by *explicitly* called functions.
- Most C implementations have included a reasonably standard collection of such functions.

- C offers straightforward, single-thread control flow: tests, loops, grouping, and subprograms, but **NOT** *multi-programming, parallel operations, synchronization, or co-routines.* Although, theses absence of some of these features may seem like a grave deficiency ("Like using a function to compare two character string") to keeping the language down to ***modest size has real benefits***. 
- Since the programming language is small, it can be described in a small space, and learned quickly. A programmer can reasonably expect to know and understand and indeed regularly use the entire language.

## G. American National Standards Institute (ANSI).
- In 1983, ANSI established a committee to provide a modern, comprehensive definition of C. Resulting in definition, the ANSI standard, or "ANSI C", was completed in the late 1988. So that most the features of the standard are already supported by modern compilers.
- Its standard based on the original reference manual. The language has a little changed; one of the goals of the standard was to make sure that most existing programs would remain valid, or, failing that, that compilers could produce warnings of new behavior.

- The most important change for the programmer is a new syntax for declaring and defining functions.
- A function declaration can now include a description of the arguments of the function; the definition syntax changes to match. This extra information makes it much easier for compilers to detect errors caused by mismatched arguments which is very useful for the language.
- Small-scale language changes including: *structure assigment* and *enumerations*.
	- Floating-point computations may now be done in single precision.
	- Arithmetic's properties, especially for unsigned types, are clarified.
	- Preprocessor is more elaborate
	--> Most of the changes will have only minor effect on most programmers.

- A second significant contribution of the standard is the ***definition of a library to accompany C***. It has a functions for interacting with operating system (read, write files), formatted input and output, memory allocation, string manipulation, and the like. 
- A collection of standard headers provides uniform access to declarations of functions and data types.

# Chapter 1: A Tutorial Introduction
---
## 1.1 Getting Started












## 1.2 Variables and Arithmetic Expressions

## 1.3 The For Statements

## 1.4 Symbolic Constants

## 1.5 Character Input and Output

## 1.6 *Arrays*

## 1.7 *Functions*

## 1.8 Arguments - Call by Value

## 1.9 Character Arrays

## 1.10 External Variables and Scope


#Patch-notes 
> - ***Last updated:17:00 Oct 14, 2026***
> - ***Location: Hoa Sen University, HCMC***