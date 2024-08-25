#include <iostream>
using namespace std;

#define MAX 100 // Define the maximum size of the stack

int top = -1; // Index of the top element
int stack[MAX]; // Array to store stack elements

// Check if the stack is empty
bool isEmpty() {
    return top == -1;
}

// Check if the stack is full
bool isFull() {
    return top == MAX - 1;
}

// Push an element onto the stack
void push(int value) {
    if (isFull()) {
        cout << "Stack Overflow! Unable to push " << value << endl;
    } else {
        stack[++top] = value; // Increment top and then add the element
        cout << value << " pushed to stack" << endl;
    }
}

// Pop an element from the stack
void pop() {
    if (isEmpty()) {
        cout << "Stack Underflow! No elements to pop" << endl;
    } else {
        cout << stack[top--] << " popped from stack" << endl;
    }
}

// Peek the top element of the stack
void peek() {
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
    } else {
        cout << "Top element is " << stack[top] << endl;
    }
}

// Display the stack elements
void display() {
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
    } else {
        cout << "Stack elements are: ";
        for (int i = 0; i <= top; i++) {
            cout << stack[i] << " ";
        }
        cout << endl;
    }
}

int main() {
    push(10); // Push elements onto the stack
    push(20);
    push(30);

    display(); // Display stack elements

    peek(); // Peek top element

    pop(); // Pop an element from the stack
    pop();
    pop();
    pop(); // Attempt to pop from an empty stack

    display(); // Display stack elements

    return 0;
}
