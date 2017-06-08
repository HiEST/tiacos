PyObject *res;
BUFSIZ=300
char *buf = PyMem_New(char, BUFSIZ); 
if (buf == NULL)
    return PyErr_NoMemory();
res = PyBytes_FromString(buf);
PyMem_Del(buf);
return res;