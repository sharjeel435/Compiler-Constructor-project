# Test Results

## Case 1

**Input:** `counter = 15`

**Expected:** counter = 15

**Intermediate Code:**

- counter = 15



**Optimized IR:**

- counter = 15



**Generated Code:**

- STORE 15 INTO counter



**Final Env:**

- counter = 15



**Passed:** ✓


## Case 2

**Input:** `balance = 100 - 45`

**Expected:** balance = 55

**Intermediate Code:**

- t1 = 100 - 45

- balance = t1



**Optimized IR:**

- t1 = 55

- balance = 55



**Generated Code:**

- LOAD 55 INTO t1

- STORE 55 INTO balance



**Final Env:**

- balance = 55

- t1 = 55



**Passed:** ✓


## Case 3

**Input:** `average = (8 + 12) / 2`

**Expected:** average = 10

**Intermediate Code:**

- t2 = 8 + 12

- t3 = t2 / 2

- average = t3



**Optimized IR:**

- t2 = 20

- t3 = 10

- average = 10



**Generated Code:**

- LOAD 20 INTO t2

- LOAD 10 INTO t3

- STORE 10 INTO average



**Final Env:**

- average = 10

- t2 = 20

- t3 = 10



**Passed:** ✓


## Case 4

**Input:** `area = 5.5 * 3.2`

**Expected:** area = 17.6

**Intermediate Code:**

- t4 = 5.5 * 3.2

- area = t4



**Optimized IR:**

- t4 = 17.6

- area = 17.6



**Generated Code:**

- LOAD 17.6 INTO t4

- STORE 17.6 INTO area



**Final Env:**

- t4 = 17.6



**Passed:** ✗


## Case 5

**Input:** `total = 25 - 5 * 2 + 8 / 4`

**Expected:** total = 17

**Intermediate Code:**

- t5 = 5 * 2

- t6 = 25 - t5

- t7 = 8 / 4

- t8 = t6 + t7

- total = t8



**Optimized IR:**

- t5 = 10

- t6 = 15

- t7 = 2

- t8 = 17

- total = 17



**Generated Code:**

- LOAD 10 INTO t5

- LOAD 15 INTO t6

- LOAD 2 INTO t7

- LOAD 17 INTO t8

- STORE 17 INTO total



**Final Env:**

- t5 = 10

- t6 = 15

- t7 = 2

- t8 = 17

- total = 17



**Passed:** ✓


## Case 6

**Input:** `calculation = ((10 - 2) * (3 + 1)) / 4`

**Expected:** calculation = 8

**Intermediate Code:**

- t9 = 10 - 2

- t10 = 3 + 1

- t11 = t9 * t10

- t12 = t11 / 4

- calculation = t12



**Optimized IR:**

- t9 = 8

- t10 = 4

- t11 = 32

- t12 = 8

- calculation = 8



**Generated Code:**

- LOAD 8 INTO t9

- LOAD 4 INTO t10

- LOAD 32 INTO t11

- LOAD 8 INTO t12

- STORE 8 INTO calculation



**Final Env:**

- calculation = 8

- t10 = 4

- t11 = 32

- t12 = 8

- t9 = 8



**Passed:** ✓


## Case 7

**Input:** `value = 2.5 * (1.2 + 3.8) - 1.5`

**Expected:** value = 11.0

**Intermediate Code:**

- t13 = 1.2 + 3.8

- t14 = 2.5 * t13

- t15 = t14 - 1.5

- value = t15



**Optimized IR:**

- t13 = 5

- t14 = 12.5

- t15 = 11

- value = 11



**Generated Code:**

- LOAD 5 INTO t13

- LOAD 12.5 INTO t14

- LOAD 11 INTO t15

- STORE 11 INTO value



**Final Env:**

- t13 = 5

- t14 = 12.5

- t15 = 11

- value = 11



**Passed:** ✓


## Case 8

**Input:** `score = 5 * 3 + 10 / 2 - 4`

**Expected:** score = 16

**Intermediate Code:**

- t16 = 5 * 3

- t17 = 10 / 2

- t18 = t16 + t17

- t19 = t18 - 4

- score = t19



**Optimized IR:**

- t16 = 15

- t17 = 5

- t18 = 20

- t19 = 16

- score = 16



**Generated Code:**

- LOAD 15 INTO t16

- LOAD 5 INTO t17

- LOAD 20 INTO t18

- LOAD 16 INTO t19

- STORE 16 INTO score



**Final Env:**

- score = 16

- t16 = 15

- t17 = 5

- t18 = 20

- t19 = 16



**Passed:** ✓


Summary: 7 / 8 passed
