#ifndef CONSTANT_EXPR_H
#define CONSTANT_EXPR_H

#include "Term.h"
#include <string>
#include <cstdint>

/* This abstract base class defines all the constant exprs
 * which includes predeined operators and numerics 
 */
class ConstantExpr : public Term
{
};

/* Predefined operators in the IR language
 */
class Operator : public ConstantExpr
{
  std::string _op;
  
 public:
  Operator(std::string op);
  ~Operator();
  std::string getOp();
  void dump(std::string prefix="");
};

/* Numerics in the IR language which includes Integers
 * and floats. For the sake of organization this was included.
 */
class Numeric : public ConstantExpr
{
};

/* Integers in the IR language
 */ 
class Integer : public Numeric
{
  int64_t _internalVal;
  
 public:
  Integer(int64_t integer);
  ~Integer();
  int64_t getInt();
  void dump(std::string prefix="");
};

/* Flating point numbers in the IR language
 */ 
class Float : public Numeric
{
  double _num;
  
 public:
  Float(double num);
  ~Float();
  double getFloat();
  void dump(std::string prefix="");
};

#endif
