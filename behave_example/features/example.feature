Feature: showing off behave

  Background:
    Given we have behave installed
    When we implement a test

  Scenario: run a simple test

    Then behave will test it for us!

  @second_test
  Scenario: Second run a simple test

    Then behave will test it for us!
    And We win this game


  Scenario: Third run a simple test

    Then behave will test it for us!


  Scenario Outline: Name Comparison
    Given User '<name>'
    When Add additional user '<name_1>'
    Then Compare Users names
    @smoke
    @regression
    Examples: first set
      | name | name_1 | name_3 |
      | Bob  | Bob    | Bob    |
      | Mike | Mike   | Mike   |
      | Bob  | Bob    | Mike   |
      | Bob  | Bob    | Bob    |
      | Bill | Bill   | Mike   |
      | Mike | Mike   | Mike   |
      | Bob  | Bob    | Mike   |

#    @regression
#    @short
#    Examples: Second set
#      | name | name_1 | name_3 |
#      | Bob  | Bob    | Bob    |
#      | Mike | Mike   | Mike   |
#      | Bob  | Mike   | Mike   |
#      | Bob  | Bob    | Bob    |
#      | Bill | Mike   | Mike   |
#      | Mike | Mike   | Mike   |
#      | Bob  | Mike   | Mike   |
