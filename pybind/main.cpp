#include <pybind11/pybind11.h>
#include calc.h

PYBIND11_MODULE(library, m) {
m.def("cntBlack", &countBlack);
m.def("cntRed", &countRed);
};