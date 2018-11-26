#ifndef CONSTANT_EXPR_H
#define CONSTANT_EXPR_H

#include "Term.h"
#include <string>
#include <cstdint>

class ConstantExpr : public Term
{
 public :
  virtual bool isOperator() = 0;
  virtual bool isInteger() = 0; 
  virtual bool isFloat() = 0;
};

/* Operators
 */
class Operator : public ConstantExpr
{
  std::string _op;
  
 public:
  Operator(std::string op);
  ~Operator();
  std::string getOp() {return _op;};
  bool isOperator() {return true;};
  bool isInteger() {return false;};
  bool isFloat() {return false;};
  void dump(std::string prefix="");
};

class Numeric : public ConstantExpr
{
};

class Integer : public Numeric
{
  int64_t _internalVal;
  
 public:
  Integer(int64_t integer);
  ~Integer();
  int64_t getInt() {return _internalVal;};
  bool isOperator() {return false;};
  bool isInteger() {return true;};
  bool isFloat() {return false;};
  void dump(std::string prefix="");
};

class Float : public Numeric
{
  double _num;
  
 public:
  Float(double num);
  ~Float();
  double getFloat() {return _num;};
  bool isOperator() {return false;};
  bool isInteger() {return false;};
  bool isFloat() {return true;};
  void dump(std::string prefix="");
};

#endif
