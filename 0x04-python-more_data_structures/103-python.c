#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - prints basic information about python lists
 * @p: python object representation of PyObject type
 * Return: nothing
 */

void print_python_list(PyObject *p)
{
	PyObject *obj;
	int i = 0;

	printf("[*] Python list info\n");
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

/**
 * print_python_bytes - prints bytes information of PyObject
 * @p: python object representation of PyObject type
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	int i;
	char *s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
	else
	{
		s = PyBytes_AS_STRING(p);
		printf("size: %zd\n", PyBytes_Size(p));
		printf("trying string: %s\n", s);

		if (PyBytes_Size(p) > 10)
		{
			printf("first 10 bytes: ");
			for (i = 0; i < 10; i++)
				printf("%x", s[i]);
		}
		else
		{
			printf("first %zd bytes: ", PyBytes_Size(p));
			for (i = 0; s[i] != '\0'; i++)
				printf("%x", s[i]);
		}
		printf("\n");
	}
}
