## Q1 | Algorithms and flowcharts | easy
In a flowchart, which shape represents a decision (a yes/no question)?
A) Rectangle
B) Oval
C) Diamond
D) Parallelogram
Answer: C

## Q2 | Algorithms and flowcharts | hard
An algorithm finds the largest of n numbers. It sets max to the first number, then compares each remaining number with max, updating max when needed. How many comparisons does it make?
A) n²
B) n - 1
C) n
D) n + 1
Answer: B

## Q3 | Control structures | easy
Which of these repeats a block of statements as long as a condition is true?
A) Variable declaration
B) if-else statement
C) Function header
D) while loop
Answer: D

## Q4 | Control structures | medium
count = 0
for i = 1 to 10:
    if i mod 2 == 0:
        count = count + 1
print count

What is printed?
A) 4
B) 5
C) 6
D) 10
Answer: B

## Q5 | Control structures | hard
total = 0
for i = 1 to 3:
    for j = 1 to i:
        total = total + 1
print total

What is printed?
A) 3
B) 5
C) 9
D) 6
Answer: D

## Q6 | Arrays | easy
An array has 5 elements and indexing starts at 0. What is the index of the last element?
A) 5
B) 6
C) 4
D) 1
Answer: C

## Q7 | Arrays | medium
arr = [4, 8, 15, 16, 23, 42]
What is arr[2] + arr[4]?
A) 38
B) 31
C) 30
D) 23
Answer: A

## Q8 | Arrays | hard
arr = [1, 2, 3, 4, 5]
for i = 0 to 3:
    arr[i] = arr[i + 1]

What does arr contain after the loop?
A) [1, 2, 3, 4, 5]
B) [2, 3, 4, 5, 1]
C) [2, 3, 4, 5, 5]
D) [2, 3, 4, 5, 6]
Answer: C

## Q9 | Variables and data types | easy
In Java, which data type is best for storing a whole number such as 25?
A) int
B) double
C) String
D) boolean
Answer: A

## Q10 | Variables and data types | medium
In Java, what is the value of x after this statement?
int x = 7 / 2;
A) 3.5
B) 3
C) 4
D) The code does not compile
Answer: B

## Q11 | Variables and data types | hard
In Java, what value does b hold after this code runs?
int a = 10;
double b = a / 4;
A) 2.5
B) 3.0
C) The code does not compile
D) 2.0
Answer: D

## Q12 | Classes and objects | easy
What is a class in object-oriented programming?
A) A variable that stores a single value
B) A blueprint or template for creating objects
C) A loop construct
D) A method that returns a value
Answer: B

## Q13 | Classes and objects | medium
In Java, what does this statement do?
Car c = new Car();
A) Declares a new class named Car
B) Imports the Car class from a library
C) Deletes an existing Car object
D) Creates a new Car object and calls its constructor
Answer: D

## Q14 | Classes and objects | hard
class Counter {
    int count = 0;
    void increment() { count++; }
}

Counter a = new Counter();
Counter b = a;
b.increment();
a.increment();
System.out.println(a.count);

What is printed?
A) 0
B) 2
C) 1
D) 3
Answer: B

## Q15 | Inheritance | easy
Which keyword does a Java class use to inherit from another class?
A) inherits
B) super
C) extends
D) implements
Answer: C

## Q16 | Inheritance | medium
class Animal { public void eat() { System.out.println("Eating"); } }
class Dog extends Animal { }

What happens when new Dog().eat() runs?
A) It runs the eat() method inherited from Animal
B) Compile error, because Dog does not define eat()
C) Runtime error
D) It creates a new Animal object
Answer: A

## Q17 | Inheritance | hard
class A { A() { System.out.print("A"); } }
class B extends A { B() { System.out.print("B"); } }

What is printed when new B(); runs?
A) A
B) B
C) BA
D) AB
Answer: D

## Q18 | Polymorphism | easy
Which statement best describes polymorphism?
A) Giving a variable and a class the same name
B) One method name or interface that behaves differently for different object types
C) Hiding data inside a class
D) Copying one class into another
Answer: B

## Q19 | Polymorphism | medium
Two methods in the same class have the same name but different parameter lists. This is called:
A) Overriding
B) Encapsulation
C) Overloading
D) Inheritance
Answer: C

## Q20 | Polymorphism | hard
class Animal { void sound() { System.out.println("Generic"); } }
class Cat extends Animal { void sound() { System.out.println("Meow"); } }

Animal x = new Cat();
x.sound();

What is printed?
A) Generic
B) Compile error
C) GenericMeow
D) Meow
Answer: D

## Q21 | Encapsulation | easy
Which Java access modifier makes a field accessible only inside its own class?
A) private
B) public
C) protected
D) static
Answer: A

## Q22 | Encapsulation | medium
Why do programmers often make fields private and provide getter and setter methods?
A) It makes the program run faster
B) It lets the class control and validate how its data is changed
C) It allows multiple inheritance
D) It stops objects from being created
Answer: B

## Q23 | Encapsulation | hard
class Account {
    private double balance = 100;
    void withdraw(double amt) {
        if (amt > 0 && amt <= balance) balance = balance - amt;
    }
    double getBalance() { return balance; }
}

Account a = new Account();
a.withdraw(150);
a.withdraw(30);
a.withdraw(-10);
System.out.println(a.getBalance());

What is printed?
A) 80.0
B) 100.0
C) -80.0
D) 70.0
Answer: D

## Q24 | Abstraction | easy
What is abstraction in object-oriented programming?
A) Showing only the essential features while hiding implementation details
B) Making all fields public
C) Copying an object into a new variable
D) Running a method repeatedly
Answer: A

## Q25 | Abstraction | hard
abstract class Shape { abstract double area(); }
class Circle extends Shape { }

What happens when this code is compiled?
A) It compiles, and area() returns 0
B) Compile error, unless Circle is also declared abstract
C) It compiles, with a runtime error when area() is called
D) Circle becomes abstract automatically
Answer: B
