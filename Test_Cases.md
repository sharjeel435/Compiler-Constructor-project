# Test Cases with Token Streams

## Test Case 1: Basic Variable Assignment
**Input:** `counter = 15`

**Token Stream:**
('IDENTIFIER', 'counter')
('ASSIGN', '=')
('NUMBER', '15')

**Expected Output:** counter = 15

---

## Test Case 2: Subtraction Operation
**Input:** `balance = 100 - 45`

**Token Stream:**
('IDENTIFIER', 'balance')
('ASSIGN', '=')
('NUMBER', '100')
('MINUS', '-')
('NUMBER', '45')

**Expected Output:** balance = 55

---

## Test Case 3: Division with Grouping
**Input:** `average = (8 + 12) / 2`

**Token Stream:**
('IDENTIFIER', 'average')
('ASSIGN', '=')
('LPAREN', '(')
('NUMBER', '8')
('PLUS', '+')
('NUMBER', '12')
('RPAREN', ')')
('DIVIDE', '/')
('NUMBER', '2')

**Expected Output:** average = 10

---

## Test Case 4: Decimal Multiplication
**Input:** `area = 5.5 * 3.2`

**Token Stream:**
('IDENTIFIER', 'area')
('ASSIGN', '=')
('NUMBER', '5.5')
('TIMES', '*')
('NUMBER', '3.2')

**Expected Output:** area = 17.6

---

## Test Case 5: Mixed Operations
**Input:** `total = 25 - 5 * 2 + 8 / 4`

**Token Stream:**
('IDENTIFIER', 'total')
('ASSIGN', '=')
('NUMBER', '25')
('MINUS', '-')
('NUMBER', '5')
('TIMES', '*')
('NUMBER', '2')
('PLUS', '+')
('NUMBER', '8')
('DIVIDE', '/')
('NUMBER', '4')

**Expected Output:** total = 17

---

## Test Case 6: Multiple Nested Groupings
**Input:** `calculation = ((10 - 2) * (3 + 1)) / 4`

**Token Stream:**
('IDENTIFIER', 'calculation')
('ASSIGN', '=')
('LPAREN', '(')
('LPAREN', '(')
('NUMBER', '10')
('MINUS', '-')
('NUMBER', '2')
('RPAREN', ')')
('TIMES', '*')
('LPAREN', '(')
('NUMBER', '3')
('PLUS', '+')
('NUMBER', '1')
('RPAREN', ')')
('RPAREN', ')')
('DIVIDE', '/')
('NUMBER', '4')

**Expected Output:** calculation = 8

---

## Test Case 7: Complex Decimal Expression
**Input:** `value = 2.5 * (1.2 + 3.8) - 1.5`

**Token Stream:**
('IDENTIFIER', 'value')
('ASSIGN', '=')
('NUMBER', '2.5')
('TIMES', '*')
('LPAREN', '(')
('NUMBER', '1.2')
('PLUS', '+')
('NUMBER', '3.8')
('RPAREN', ')')
('MINUS', '-')
('NUMBER', '1.5')

**Expected Output:** value = 11.0

---

## Test Case 8: Chained Operations
**Input:** `score = 5 * 3 + 10 / 2 - 4`

**Token Stream:**
('IDENTIFIER', 'score')
('ASSIGN', '=')
('NUMBER', '5')
('TIMES', '*')
('NUMBER', '3')
('PLUS', '+')
('NUMBER', '10')
('DIVIDE', '/')
('NUMBER', '2')
('MINUS', '-')
('NUMBER', '4')

**Expected Output:** score = 16