Feature: Testing Suma Requests

  Scenario Outline: Suma Get
    Given dada la URL
    When se hace request GET con los parametros A = <a> y B = <b>
    Then el resultado es <c>

    Examples:
    |a  |b  |c  |
    |1  |2  |3  |
    |20 |22 |42 |
    |5  |9  |14 |


  Scenario: Suma Post
    Given dada la URL
    When se hace request POST con los parametros A = 1 y B = 2
    Then el resultado es 3

  Scenario: Suma Post
    Given dada la URL
    When se hace request POST con los parametros A = a y B = b
    Then el resultado es 3