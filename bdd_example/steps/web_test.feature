Feature: Blog
  A site where you can publish your articles.

  @api
  Scenario: Get request to page
    Given I'm an user 'Test1'
    And I have endpoint'https://www.aqa.science/admin/login/'

    When I go to endpoint page

    Then I should receive '200' code


  Scenario: Get Request to wrong page
    Given I'm an user 'Test2'
    And I have endpoint'https://www.aqa.science//'

    When I go to endpoint page

    Then I should receive '403' code

  Scenario: Get Request to wrong page 404
    Given I'm an user 'Test2'
    And I have endpoint'https://www.google.com/a'

    When I go to endpoint page

    Then I should receive '404' code


