// C++ code
#include <iostream>
#include <vector>

void swap(int &p1, int &p2){
    int temp = p1;
    p1 = p2;
    p2 = temp;
}

void MaxHeapify(std::vector<int> &array, int root, int length){

    int left = 2*root,      // ���oleft child
    right = 2*root + 1,     // ���oright child
    largest;                // largest�ΨӰO���]�troot�Pchild, �T�̤���Key�̤j��node

    if (left <= length && array[left] > array[root])
        largest = left;
    else
        largest = root;

    if (right <= length && array[right] > array[largest])
        largest = right;

    if (largest != root) {                         // �p�G�ثeroot��Key���O�T�̤����̤j
        swap(array[largest], array[root]);         // �N�մ�root�P�T�̤�Key�̤j��node����m
        MaxHeapify(array, largest, length);        // �վ�s��subtree��Max Heap
    }
}

void BuildMaxHeap(std::vector<int> &array){

    for (int i = (int)array.size()/2; i >= 1 ; i--) {
        MaxHeapify(array, i, (int)array.size() - 1);     // length�n��@, �]��heap�q1�}�l�s����
    }
}

void HeapSort(std::vector<int> &array){

    array.insert(array.begin(), 0);                     // �Nindex(0)���m

    BuildMaxHeap(array);                                // �Narray�վ㦨Max Heap

    int size = (int)array.size() -1;                    // size�ΨӰO���u�ثe�n�B�z���x�}�v������
    for (int i = (int)array.size() -1; i >= 2; i--) {
        swap(array[1], array[i]);                       // �N�̤j�ȩ��array���̫�@�Ӧ�m
        size--;
        MaxHeapify(array, 1, size);                     // �վ�u�����̫�@�Ӧ�m�v���x�}
    }

    array.erase(array.begin());                         // �Nindex(0)�R��
}

void PrintArray(std::vector<int> &array){
    for (int i = 0; i < array.size(); i++) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}

int main() {

    int arr = {9, 4, 1, 6, 7, 3, 8, 2, 5};
    std::vector<int> array(arr, arr+sizeof(arr)/sizeof(int));

    std::cout << "original:\n";
    PrintArray(array);

    HeapSort(array);

    std::cout << "sorted:\n";
    PrintArray(array);

    return 0;
}
