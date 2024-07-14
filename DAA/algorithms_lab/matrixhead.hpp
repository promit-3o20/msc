#ifndef MatrixHead_HPP
#define MatrixHead_HPP

#include <iostream>
#include <vector>

using namespace std;

// Functions...............................................................................
// Input
void inputMatrix(vector<vector<int>> &matrix, int m, int n)
{
    for (int i = 0; i < m; i++)
    {
        vector<int> row(n);
        for (int j = 0; j < n; j++)
        {
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> row[j];
        }
        matrix.push_back(row);
    }
}
// Output
void outputMatrix(const vector<vector<int>> &matrix)
{
    for (const auto &row : matrix)
    {
        for (const auto &elem : row)
        {
            cout << elem << " ";
        }
        cout << endl;
    }
}
// Addition
vector<vector<int>> addMatrix(const vector<vector<int>> &mat1, const vector<vector<int>> &mat2, vector<vector<int>> &result_mat, int rs, int re, int cs, int ce)
{

    if (re - rs == 1)
    {
        result_mat[rs][cs] = mat1[rs][cs] + mat2[rs][cs];
    }
    else
    {
        addMatrix(mat1, mat2, result_mat, rs, (rs + re) / 2, cs, (cs + ce) / 2);
        addMatrix(mat1, mat2, result_mat, rs, (rs + re) / 2, (cs + ce) / 2, ce);
        addMatrix(mat1, mat2, result_mat, (rs + re) / 2, re, cs, (cs + ce) / 2);
        addMatrix(mat1, mat2, result_mat, (rs + re) / 2, re, (cs + ce) / 2, ce);
    }
    return result_mat;
}
// Subtraction
vector<vector<int>> subtractMatrix(const vector<vector<int>> &mat1, const vector<vector<int>> &mat2, vector<vector<int>> &result_mat, int rs, int re, int cs, int ce)
{

    if (re - rs == 1)
    {
        result_mat[rs][cs] = mat1[rs][cs] - mat2[rs][cs];
    }
    else
    {
        subtractMatrix(mat1, mat2, result_mat, rs, (rs + re) / 2, cs, (cs + ce) / 2);
        subtractMatrix(mat1, mat2, result_mat, rs, (rs + re) / 2, (cs + ce) / 2, ce);
        subtractMatrix(mat1, mat2, result_mat, (rs + re) / 2, re, cs, (cs + ce) / 2);
        subtractMatrix(mat1, mat2, result_mat, (rs + re) / 2, re, (cs + ce) / 2, ce);
    }
    return result_mat;
}
// Multiplication
vector<vector<int>> multiplyMatrix(const vector<vector<int>> &mat1, const vector<vector<int>> &mat2, vector<vector<int>> &result_mat, int mat1_rs, int mat1_re, int mat1_cs, int mat1_ce, int mat2_rs, int mat2_re, int mat2_cs, int mat2_ce)
{
    if (mat1_re - mat1_rs == 1)
    {
        result_mat[mat1_rs][mat2_cs] += mat1[mat1_rs][mat1_cs] * mat2[mat1_cs][mat2_cs];
    }
    else
    {
        multiplyMatrix(mat1, mat2, result_mat, mat1_rs, (mat1_rs + mat1_re) / 2, mat1_cs, (mat1_cs + mat1_ce) / 2, mat2_rs, (mat2_rs + mat2_re) / 2, mat2_cs, (mat2_cs + mat2_ce) / 2);
        multiplyMatrix(mat1, mat2, result_mat, mat1_rs, (mat1_rs + mat1_re) / 2, (mat1_cs + mat1_ce) / 2, mat1_ce, (mat2_rs + mat2_re) / 2, mat2_re, mat2_cs, (mat2_cs + mat2_ce) / 2);
        multiplyMatrix(mat1, mat2, result_mat, mat1_rs, (mat1_rs + mat1_re) / 2, mat1_cs, (mat1_cs + mat1_ce) / 2, mat2_rs, (mat2_rs + mat2_re) / 2, (mat2_cs + mat2_ce) / 2, mat2_cs);
        multiplyMatrix(mat1, mat2, result_mat, mat1_rs, (mat1_rs + mat1_re) / 2, (mat1_cs + mat1_ce) / 2, mat1_ce, (mat2_rs + mat2_re) / 2, mat2_re, (mat2_cs + mat2_ce) / 2, mat2_ce);
        multiplyMatrix(mat1, mat2, result_mat, (mat1_rs + mat1_re) / 2, mat1_re, mat1_cs, (mat1_cs + mat1_ce) / 2, mat2_rs, (mat2_rs + mat2_re) / 2, mat2_cs, (mat2_cs + mat2_ce) / 2);
        multiplyMatrix(mat1, mat2, result_mat, (mat1_rs + mat1_re) / 2, mat1_re, (mat1_cs + mat1_ce) / 2, mat1_ce, (mat2_rs + mat2_re) / 2, mat2_re, mat2_cs, (mat2_cs + mat2_ce) / 2);
        multiplyMatrix(mat1, mat2, result_mat, (mat1_rs + mat1_re) / 2, mat1_re, mat1_cs, (mat1_cs + mat1_ce) / 2, mat2_rs, (mat2_rs + mat2_re) / 2, (mat2_cs + mat2_ce) / 2, mat2_ce);
        multiplyMatrix(mat1, mat2, result_mat, (mat1_rs + mat1_re) / 2, mat1_re, (mat1_cs + mat1_ce) / 2, mat1_ce, (mat2_rs + mat2_re) / 2, mat2_re, (mat2_cs + mat2_ce) / 2, mat2_ce);
    }
    return result_mat;
}

#endif