# CkFinder

## Roll No : CS20B025

## Name    : Nishanth

Content
==========================================

### Input [**cs20b025_fd.txt**]

### Functional dependencies

```
{'A'} ==> {'C', 'B'}
{'A', 'B'} ==> {'E'}
{'C'} ==> {'D', 'E'}
{'E'} ==> {'A'}
```

### Candidate Keys

```
 1) AF
 2) FE
 3) FC
```

### Rule

> no rule

### Prime Attributes

```
ACEF
```

### Non-Prime Attributes

```
BD
```

### Input [**cs20b025_input1NF.txt**]

### Functional dependencies

```
{'A'} ==> {'C'}
{'B'} ==> {'C'}
{'D'} ==> {'B'}
```

### Candidate Keys

```
 1) AD
```

### Rule

> we can assume every fd obey it becoz it is our preference

### Prime Attributes

```
AD
```

### Non-Prime Attributes

```
CB
```

### Input [**cs20b025_input2NF.txt**]

### Functional dependencies

```
{'A'} ==> {'B'}
{'B'} ==> {'C'}
{'C'} ==> {'A'}
```

### Candidate Keys

```
 1) AD
 2) CD
 3) BD
```

### Rule 

> cycle in functional dependencies required because we shouldn't have partial dependencies

### Prime Attributes

```
ABCD
```

### Non-Prime Attributes

```
None
```

### Input [**cs20b025_input3NF.txt**]

### Functional dependencies

```
{'A'} ==> {'B'}
{'B'} ==> {'A'}
{'C'} ==> {'D'}
{'D'} ==> {'C'}
```

### Candidate Keys

```
 1) AC
 2) AD
 3) CB
 4) BD
```

### Rule

> it must contain cycle as well (it obeys 2NF) but cycle of length more than 2 gets transitive dependency so we need to avoid it, thus cycle length must always be 2

### Prime Attributes

```
ABCD
```

### Non-Prime Attributes

```
None
```

### Input [**cs20b025_inputBCNF.txt**]

### Functional dependencies

```
{'A'} ==> {'B'}
{'C'} ==> {'D'}
```

### Candidate Keys

```
 1) AC
```

### Rule

> any valid 2NF can be considered BCNF

### Prime Attributes

```
AC
```

### Non-Prime Attributes

```
BD
```
