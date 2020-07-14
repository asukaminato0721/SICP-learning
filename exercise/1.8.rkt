#lang sicp

(define (eps x y)
  (if (and (<(- x (* y y y)) 0.0001); -0.0001<x-y<0.0001
           (>(- x (* y y y)) -0.0001)
           )
      #t #f
      ))

(define (temp x y)
  (if (eps x y) y
      (temp x (/ (+ (/ x (* y y)) (* 2 y)) 3))
      )
  )
(define (1-8 a)
  (temp a 1.9)
  )
(1-8 6)