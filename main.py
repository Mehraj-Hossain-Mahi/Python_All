#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
}*head;

void input(int n)
{
    struct node *newnode,*temp;
    int data,i;
    head = (struct node*)malloc(sizeof(struct node));
    if (head== NULL)
    {
        printf("Memory Does not Allocated");
        exit(0);
    }
    printf("Enter the Data of Node 1 : ");
    scanf("%d",&data);
    head->data = data;
    head->next = NULL;

    temp = head;
    for(i=2; i<=n; i++)
    {
        newnode = (struct node*)malloc(sizeof(struct node));

        if (newnode==NULL)
        {
            printf("Memory Does not Allocated");
            break;
        }

        printf("Enter the data of Node %d : ",i);
        scanf("%d",&data);
        newnode->data = data;
        newnode->next = NULL;

        temp->next = newnode;
        temp = temp->next;
    }
}

void output()
{
    struct node *temp;

    if (temp == NULL)
    {
        printf("The list is Empty ");
    }
    temp = head;
    while(temp!=NULL)
    {
        printf("Data : %d\n",temp->data);
        temp = temp->next;
    }
}
int main()
{
    int n,i;
    printf("Enter the Number of N : ");
    scanf("%d",&n);
    input(n);
    output();
    return 0;

}
