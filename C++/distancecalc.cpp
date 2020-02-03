#include<iostream>
#include"distancecalc.h"
using namespace std;

int main()
{
	double a[3] = {1.0, 2.0, 3.0};
	double b[3] = {4.0, 5.0, 6.0};
	cout << distance3d(a, b) << endl;
}