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
	Py_ssize_t size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		s = PyBytes_AS_STRING(p);
		size = PyBytes_Size(p);

		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", s);

		if (size > 10)
		{
			printf("  first 10 bytes: ");
			for (i = 0; i < 10; i++)
			{
				printf("%x", s[i]);
				if (i < 9)
					printf(" ");
			}
		}
		else
		{
			printf("  first %zd bytes: ", (size + 1));
			for (i = 0; i <= (size + 1); i++)
			{
				printf("%x", s[i]);
				if (i < (size))
					printf(" ");
			}
		}
		printf("\n");
	}
}
