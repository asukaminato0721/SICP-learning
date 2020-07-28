#lang sicp

(define (make-account balance password)
  
  (define(withdraw amount)
    (if(>= balance amount)
       (begin
         (set! balance(- balance amount))    balance)
       "Insufficientfunds"
       )
    )
  
  (define(deposit amount)
    (set! balance ( + balance amount))balance
    )
  (define(dispatch pw m)
    (cond[(and (eq? pw password)(eq? m 'withdraw)) withdraw]
         [(and (eq? m 'deposit)(eq? pw password)) deposit]
         [(not (eq? pw password))(error "incorrect-password")]
         [else (error "Unknownrequest:MAKE-ACCOUNT" m)]
         )
    )
  dispatch
  )
(define acc(make-account 100 'sp))
((acc 'sp 'withdraw ) 50)
((acc 'sm 'withdraw) 60)
