Feature: Feature Requests

 Scenario: suma GET
   Given una URL
   When se hace una request GET con los parametros A = 1 y B = 2
   Then el resultado es 3

 Scenario: suma POST
   Given una URL
   When se hace una request POST con los parametros A = 1 y B = 2
   Then el resultado es 3