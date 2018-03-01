# Translation of SMT2 horn clauses to other formats

To setup z3:
```
pip installl -r requirements.txt
```

To test
```
$ cat test/inline_test.smt2 

(set-logic HORN)
(set-info :status sat)
(declare-fun p (Int) Bool)
(declare-fun q (Int) Bool)
(assert (forall ((x Int)) (=> (> x 0) (p x))))
(assert (forall ((x Int)) (=> (p x) (q x))))
(assert (forall ((x Int)) (=> (q x) (> x 0))))

$ python translate.py test/inline_test.smt2

(declare-fun q (Int) Bool)
(assert (forall ((A Int)) (=> (not (<= A 0)) (q A))))
(assert (forall ((A Int)) (=> (and (q A) (<= A 0)) false)))
```

