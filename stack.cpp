#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define maximum size of the stack

int stack[MAX];
int top = -1;  // Initialize top to -1, indicating the stack is empty

// Function to add an element to the stack
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push %d onto the stack.\n", value);
    } else {
        top++;
        stack[top] = value;
        printf("%d pushed onto the stack.\n", value);
    }
}

// Function to remove an element from the stack
int pop() {
    if (top == -1) {
        printf("Stack Underflow! Cannot pop from the stack.\n");
        return -1;
    } else {
        int popped_value = stack[top];
        top--;
        return popped_value;
    }
}

// Function to return the top element of the stack without removing it
int peek() {
    if (top == -1) {
        printf("Stack is empty. Nothing to peek.\n");
        return -1;
    } else {
        return stack[top];
    }
}

// Function to display all elements in the stack
void display() {
    if (top == -1) {
        printf("Stack is empty.\n");
    } else {
        printf("Stack elements are: \n");
        for (int i = top; i >= 0; i--) {
            printf("%d\n", stack[i]);
        }
    }
}

int main() {
    int choice, value;

    while(1) {
        printf("\n--- Stack Operations Menu ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter the value to push: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                value = pop();
                if (value != -1) {
                    printf("Popped value: %d\n", value);
                }
                break;
            case 3:
                value = peek();
                if (value != -1) {
                    printf("Top element is: %d\n", value);
                }
                break;
            case 4:
                display();
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
