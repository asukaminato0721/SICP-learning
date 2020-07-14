#lang racket


(define( sum-of-2-sq a b)
  (+(*  a a)
    (*  b b))
    )
(define (2-large a b c)
  (cond ((and (>= a b) (>= b c))   ( sum-of-2-sq a b))
        ((and (>= b a) (>= c a))   ( sum-of-2-sq c b))
        ((and (>= c b) (>= a b))   ( sum-of-2-sq a c))
        )
  )
(2-large 1 2 3)
;注意最好别返回多个值，有点坑
