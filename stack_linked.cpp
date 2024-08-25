#include <iostream>
using namespace std;

// Define a node of the stack
struct Node {
    int data;
    Node* next;
};
Node* top=NULL;
bool isEmpty() {
    return top == nullptr;
}
// Push an element onto the stack
void push(int value) {
    Node* newnode=new Node;
    newnode->data=value;
    newnode->next=top;
    top=newnode;
    cout << value << " pushed to stack" << endl;
}
// Pop an element from the stack
void pop() {
    if(isEmpty()) cout<<"empty"<< endl;
    else
    {
        Node* temp=top;
        top=top->next;
        cout << temp->data << " popped from stack" << endl;
        delete temp;
    }
}

// Peek the top element of the stack
void peek() {
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
        return;
    }
    cout << "Top element is " << top->data << endl;
}

// Display the stack elements
void display() {
    if (isEmpty()) {
        cout << "Stack is empty" << endl;
        return;
    }
    Node* temp = top;
    cout << "Stack elements are: ";
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
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
