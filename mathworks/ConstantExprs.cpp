#include "ConstantExprs.h"
#include <iostream>

Operator::Operator(std::string op) :
  _op(op)
{
}

Operator::~Operator()
{
}

void Operator::dump(std::string prefix)
{
  std::cout << prefix << "Operator: " << _op << std::endl;
}

Integer::Integer(int64_t integer) :
  _internalVal(integer)
{
}

Integer::~Integer()
{
}

void Integer::dump(std::string prefix)
{
  std::cout << prefix << "Integer: " << _internalVal << std::endl;
}

Float::Float(double num) :
  _num(num)
{
}

Float::~Float()
{
}

void Float::dump(std::string prefix)
{
  std::cout << prefix << "Float: " << _num << std::endl; 
}
