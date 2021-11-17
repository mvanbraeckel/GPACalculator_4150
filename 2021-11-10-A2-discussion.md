
# Issues with A2:

* definitely written very badly.  It is incoherent, and doens't focus well.

* actual objective not clear:
	- consider how state machines help you think about code
	- consider how constructing a state machine will help you make test ases to assess whether the state is maintained
	- think about how the design of this code base affects your ability to assess whether the states are working


## Tasks:

* write out a state machine
	- that captures all the state changes relevant to calculating GPA
	- with some limits so that it isn't huge:
		- max one term
		- max two courses
		- only three grades: A, B, F

* identify how you will build test cases to assess your state machine
	- intention was do *design* these:
		- specify calls, required arguments and expected outputs for
				your test cases

	- identify whether and how things change between languages


## Confusions:

* by talking about writing code, the following incorrect messages were sent:
	- this is about coding (not design)
	- this is about struggling to solve issues with (broken) code
		- in this course, we never will try and fix code given out
		- at most, we simply say "it is all broken"
		- for the python implementation, that is accidentally true here


# Suggestion/What I am looking for:

- a state machine:
	- labelled so that we can tell:
		- what your states actually mean
		- what causes the transitions
	- should capture the system as described within the limits

- a set of tests:
	- can simply be a document outlining:
		- what the test is supposed to be testing
		- what calls with what arguments will be made
		- what the expected value is
		- whether this is done differently in Java/Python




       X        
      / \      
     A   B     
      \ /      
       0        
                
	 -----
    |     |
    |  X  |     
    | /|\ |    
     A | B|    
      \|/      
       0        
                
	



