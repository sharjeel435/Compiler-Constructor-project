# MathScript Language Specification

## 1. Language Overview
**Name:** MathScript  
**Purpose:** A domain-specific language designed for computing mathematical expressions and storing outcomes in variables.  
**Domain:** Educational computational tool for expression evaluation

## 2. Language Features
- Variable assignment operations
- Basic arithmetic computations (addition, subtraction, multiplication, division)
- Parenthetical grouping for expression organization
- Support for both integer and floating-point numerical values

## 3. Keywords
This expression-based language operates without reserved keywords

## 4. Operators
| Operator | Function | Precedence Level | Associativity |
|----------|----------|------------------|---------------|
| = | Variable assignment | 1 (Lowest) | Right-to-left |
| + | Arithmetic addition | 2 | Left-to-right |
| - | Arithmetic subtraction | 2 | Left-to-right |
| * | Arithmetic multiplication | 3 | Left-to-right |
| / | Arithmetic division | 3 | Left-to-right |
| ( ) | Expression grouping | 4 (Highest) | Not applicable |

## 5. Data Types
- **NUMBER**: Integer values (examples: 5, -10) or Floating-point values (examples: 3.14, -2.5)
- **IDENTIFIER**: Variable identifiers (examples: x, computation_result, userVariable)

## 6. Lexical Rules

### Token Definitions:
- **NUMBER**: `\d+(\.\d+)?` - recognizes 15, 3.14159, 250.75
- **IDENTIFIER**: `[A-Za-z][A-Za-z0-9]*` - recognizes variable, data2, output_value
- **PLUS**: `\+`
- **MINUS**: `-`
- **TIMES**: `\*`
- **DIVIDE**: `/`
- **ASSIGN**: `=`
- **LPAREN**: `\(`
- **RPAREN**: `\)`

## 7. Sample Implementations
### Implementation 1:
**Input Expression:** `x = 5`  
**Computation Result:** Variable x now contains the numerical value 5

### Implementation 2:
**Input Expression:** `y = 10 + 20`  
**Computation Result:** Variable y now contains the computed value 30

### Implementation 3:
**Input Expression:** `computation_result = (5 + 3) * 2`  
**Computation Result:** Variable computation_result now contains the calculated value 16