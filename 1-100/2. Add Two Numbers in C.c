
struct ListNode *new(int data)//�ҥ�c++��new���
{
    struct ListNode *NewNode = (struct ListNode *) malloc(sizeof(struct ListNode));
    NewNode->val = data;
    NewNode->next = NULL;
    return NewNode;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

   struct ListNode *l3 = new (0);  //�ŧi�^�ǦC�`��C
        struct ListNode *p = l1, *q = l2, *r = l3;  //�ŧi�쵲��C����
        int carry = 0, sum = 0;  //�ŧi�[�`�H�ζi��Ȧs

        while(p != NULL && q != NULL)  //�Y���쵲��C�Ҧ���
        {
            sum = p->val + q->val + carry;  //��X��Ӧ�ƥH�ζi�줧�`�M
            carry = sum / 10;  //��X�i���
            r->next = new (sum % 10);  //�Х߸Ӧ�Ƥ��`�I
            p = p->next;  //���ʫ���
            q = q->next;
            r = r->next;
        }

        while(p != NULL || q != NULL || carry != 0)  //�Y�٦��@���쵲��C���ȥH���٦��i��
        {
            sum = carry;
            if (p != NULL)  //�Yl1���O�Ū�
            {
                sum += p->val;
                p = p->next;
            }
            if (q != NULL)  //�Yl2���O�Ū�
            {
                sum += q->val;
                q = q->next;
            }
            carry = sum / 10;  //�p��i��
            r->next = new (sum % 10);  //�Х߸`�I
            r = r->next;
        }

        return l3->next;
    }
