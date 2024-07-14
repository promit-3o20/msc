#include <iostream>
#include <vector>
#include "matrixhead.hpp"

using namespace std;

int main()
{
    // Declare variabls.
    int m1, n1, m2, n2;
    // Take input from user for matrix dimention m x n.
    do
    {
        cout << "Enter the row and column of First matrix A: ";
        cin >> m1 >> n1;
        cout << "Enter the row and column of Second matrix B: ";
        cin >> m2 >> n2;
    } while (n2 != m1);
    
    // Declare the matrix.
    vector<vector<int>> mat1;
    vector<vector<int>> mat2;
    vector<vector<int>> result_mat(m1, vector<int>(n2, 0));

    // Call inoutMatrix() and outputMatrix().
    cout << "Input the elements of first matrix (" << m1 << "x" << n1 << ")" << endl;
    inputMatrix(mat1, m1, n1);
    cout << "First Matrix (" << m1 << "x" << n1 << ")" << endl;
    outputMatrix(mat1);
    cout << "Input the elements of second matrix (" << m2 << "x" << n2 << ")" << endl;
    inputMatrix(mat2, m2, n2);
    cout << "Second Matrix (" << m2 << "x" << n2 << ")" << endl;
    outputMatrix(mat2);
    // Call matrixMultiply() and display multiplied matrix using outputMatrix().
    multiplyMatrix(mat1, mat2, result_mat, 0, m1, 0, n1, 0, m2, 0, n2);
    cout << "Resultant matrix C -->\n";
    outputMatrix(result_mat);

    return 0;
}