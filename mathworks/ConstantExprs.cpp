#include "ConstantExprs.h"
#include <iostream>

Operator::Operator(std::string op, std::vector<Term*> *operands) :
  _op(op),
  _operands(operands)
{
}

Operator::~Operator()
{
}

void Operator::dump()
{
  std::cout << "+Operator: " << _op << std::endl;
  for (std::vector<Term *>::const_iterator c_it = _operands->begin();
       c_it != _operands->end(); ++c_it) {
    std::cout << "|-";
    (*c_it)->dump();
  }
}

Integer::Integer(int64_t integer) :
  _internalVal(integer)
{
}

Integer::~Integer()
{
}

void Integer::dump()
{
  std::cout << "Integer: " << _internalVal << std::endl;
}

Float::Float(double num) :
  _num(num)
{
}

Float::~Float()
{
}

void Float::dump()
{
  std::cout << "Float: " << _num << std::endl; 
}
