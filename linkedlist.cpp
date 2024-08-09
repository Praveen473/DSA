#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};
void  deletenode(Node*& head,int value,int position)
{
    Node* temp=head;
    for(int i=0;i<position-1;i++)
    {
        temp=temp->next;
    }
    Node* nodetodelete=temp->next;
    temp->next=temp->next->next;
    delete nodetodelete;
    
}
void  insert_at_pos(Node*& head,int value,int position)
{
    Node* newnode=new Node;
    newnode->data=value;
    newnode->next=NULL;
    Node* temp=head;
    for(int i=0;i<position-1;i++)
    {
        temp=temp->next;
    }
    newnode->next=temp->next;
    temp->next=newnode;
}
void  insert_at_end(Node*& head,int value)
{
    Node* newnode=new Node;
    newnode->data=value;
    newnode->next=NULL;
    Node* temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;
}
void insert_at_beg(Node*& head,int value)
{
    Node* newnode=new Node;
    newnode->data=value;
    newnode->next=NULL;
    newnode->next=head;
    head=newnode;
    

}
void print(Node* head)
{
    Node* temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
}
int main()
{
    Node* head=new Node;
    head->data=10;
    head->next=NULL;

    Node* temp=head;
    for(int i=20;i<60;i += 10)
    {
        Node* temp1=new Node;
        temp1->data=i;
        temp1->next=NULL;
        temp->next=temp1;
        temp=temp1;
    }

    print(head);

    insert_at_beg(head,5);
    print(head);
    insert_at_end(head,55);
    print(head);
    insert_at_pos(head,24,3);
    print(head);
    deletenode(head,24,3);
    print(head);
    return 0;

}
