Feature: Blog
  A site where you can publish your articles.

  Scenario Outline: Get request to page
    Given I'm an user '<user>'
    And I have endpoint '<url>'

    When I go to endpoint page

    Then I should receive '<code>' code

    @smoke
    Examples:
      | user  | url                           | code |
      | Test1 | https://www.aqa.science/admin | 200  |
      | Test2 | https://www.aqa.science//     | 403  |
      | Test2 | https://www.google.com/a      | 404  |
      | Test2 | https://www.google.com/       | 200  |

    @extended
    Examples:
      | user  | url                           | code |
      | Test1 | https://www.aqa.science/admin | 200  |
      | Test2 | https://www.google.com/a      | 404  |
      | Test2 | https://www.google.com/       | 200  |


  Scenario: Get Request to wrong page
    Given I'm an user 'Test2'
    And I have endpoint 'https://www.aqa.science//'

    When I go to endpoint page

    Then I should receive '403' code

  Scenario: Get Request to wrong page 404
    Given I'm an user 'Test2'
    And I have endpoint 'https://www.google.com/a'

    When I go to endpoint page

    Then I should receive '404' code



