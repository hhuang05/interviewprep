#ifndef TERM_H
#define TERM_H

#include <map>
#include <string>
#include <vector>

// These definitions will be used for floating point comparisons
#define Abs(x)    ((x) < 0 ? -(x) : (x))
#define Max(a, b) ((a) > (b) ? (a) : (b))

typedef std::map<std::string, std::string> VariableMap;

/* Term: Abstract base class of all concrete terms
 * 
 */
class Term
{

public:
  /** 
   * Checks to see if two Terms are isomorphic by recursively
   * checking substructures.  
   *
   * @param term1 - First term
   * @param term2 - Second term
   * @param varMap - Optional VariableMap specifically use during function
   * definition comparisons to check variable order
   */
  static bool IsIsomorphic(Term *term1, Term *term2,
                           VariableMap *varMap=nullptr);

  // Prints each specific term to stdout
  virtual void dump(std::string prefix="") = 0;
};

#endif
