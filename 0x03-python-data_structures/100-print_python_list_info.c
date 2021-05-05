#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - prints basic information about python lists
 * @p: python object representation of objects of certain types
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int i = 0;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	}

	while (i < PyList_Size(p))
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
