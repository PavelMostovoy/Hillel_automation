# Created by pmostovoi at 5/19/22
Feature: Second Feathure
  # Enter feature description here

  Scenario Outline: Name Comparison
    Given User '<name>'
    When Add additional user '<name_1>'
    Then Compare Users names
    Examples:
      | name | name_1 |
      | Bob  | Bob    |
      | Bill | Mike   |
      | Mike | Mike   |
      | Bob  | Mike   |
      | Bob  | Bob    |
      | Bill | Mike   |
      | Mike | Mike   |
      | Bob  | Mike   |
      | Bob  | Bob    |
      | Bill | Mike   |
      | Mike | Mike   |
      | Bob  | Mike   |
      | Bob  | Bob    |
      | Bill | Mike   |
      | Mike | Mike   |
      | Bob  | Mike   |