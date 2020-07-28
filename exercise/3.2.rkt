#lang sicp

(define (make-monitored func)
  (begin (define count 0)
         (lambda (x)
           (cond [(eq? x 'how-many-calls?)
                  (begin
                    (set! count (+ 1 count))
                    count
                    )
                  ]
                 [(number? x)(func x)]
                 )
           )
         )
  )
(define  s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)
(s 20)
(s 'how-many-calls?)
