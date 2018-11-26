#include "ConstantExprs.h"
#include <iostream>

/****** Operator Class Methods ******/

Operator::Operator(std::string op) :
  _op(op)
{
}

Operator::~Operator()
{
}

std::string Operator::getOp()
{
  return _op;
}

void Operator::dump(std::string prefix)
{
  std::cout << prefix << "Operator: " << _op << std::endl;
}

/****** Integer Class Methods ******/

Integer::Integer(int64_t integer) :
  _internalVal(integer)
{
}

Integer::~Integer()
{
}

int64_t Integer::getInt()
{
  return _internalVal;
}

void Integer::dump(std::string prefix)
{
  std::cout << prefix << "Integer: " << _internalVal << std::endl;
}

/****** Float Class Methods ******/

Float::Float(double num) :
  _num(num)
{
}

Float::~Float()
{
}

double Float::getFloat()
{
  return _num;
}

void Float::dump(std::string prefix)
{
  std::cout << prefix << "Float: " << _num << std::endl; 
}
