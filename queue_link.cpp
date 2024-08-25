#include <iostream>
using namespace std;

// Node structure for linked list
struct Node {
    int data;
    Node* next;
};

// Queue structure
struct QueueLinkedList {
    Node* front;
    Node* rear;
};

// Initialize the queue
void initQueue(QueueLinkedList &q) {
    q.front = nullptr;
    q.rear = nullptr;
}

// Check if the queue is empty
bool isEmpty(QueueLinkedList &q) {
    return q.front == nullptr;
}

// Add an element to the queue
void enqueue(QueueLinkedList &q, int element) {
    Node* newNode = new Node();
    newNode->data = element;
    newNode->next = nullptr;
    if (isEmpty(q)) {
        q.front = newNode;
        q.rear = newNode;
    } else {
        q.rear->next = newNode;
        q.rear = newNode;
    }
}

// Remove an element from the queue
int dequeue(QueueLinkedList &q) {
    if (isEmpty(q)) {
        cout << "Queue is empty!" << endl;
        return -1; // Return -1 or some error value
    }
    Node* temp = q.front;
    int element = temp->data;
    q.front = q.front->next;
    if (q.front == nullptr) {
        q.rear = nullptr;
    }
    delete temp;
    return element;
}

// Get the front element of the queue
int peek(QueueLinkedList &q) {
    if (isEmpty(q)) {
        cout << "Queue is empty!" << endl;
        return -1; // Return -1 or some error value
    }
    return q.front->data;
}

// Example usage
int main() {
    QueueLinkedList q;
    initQueue(q);

    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);

    cout << "Front element: " << peek(q) << endl; // Should print 10

    cout << "Dequeued: " << dequeue(q) << endl; // Should print 10
    cout << "Dequeued: " << dequeue(q) << endl; // Should print 20

    return 0;
}
