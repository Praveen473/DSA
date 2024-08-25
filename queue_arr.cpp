#include <iostream>
using namespace std;

#define MAX 100 // Define the maximum size of the queue

// Queue using a fixed-size array
struct QueueArray {
    int front, rear, size;
    int array[MAX];
};

// Initialize the queue
void initQueue(QueueArray &q) {
    q.front = 0;
    q.rear = -1;
    q.size = 0;
}

// Check if the queue is empty
bool isEmpty(QueueArray &q) {
    return q.size == 0;
}

// Check if the queue is full
bool isFull(QueueArray &q) {
    return q.size == MAX;
}

// Add an element to the queue
void enqueue(QueueArray &q, int element) {
    if (isFull(q)) {
        cout << "Queue is full!" << endl;
        return;
    }
    q.rear = (q.rear + 1) % MAX;
    q.array[q.rear] = element;
    q.size++;
}

// Remove an element from the queue
int dequeue(QueueArray &q) {
    if (isEmpty(q)) {
        cout << "Queue is empty!" << endl;
        return -1; // Return -1 or some error value
    }
    int element = q.array[q.front];
    q.front = (q.front + 1) % MAX;
    q.size--;
    return element;
}

// Get the front element of the queue
int peek(QueueArray &q) {
    if (isEmpty(q)) {
        cout << "Queue is empty!" << endl;
        return -1; // Return -1 or some error value
    }
    return q.array[q.front];
}

// Example usage
int main() {
    QueueArray q;
    initQueue(q);

    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);

    cout << "Front element: " << peek(q) << endl; // Should print 10

    cout << "Dequeued: " << dequeue(q) << endl; // Should print 10
    cout << "Dequeued: " << dequeue(q) << endl; // Should print 20

    return 0;
}
