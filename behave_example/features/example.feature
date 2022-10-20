Feature: showing off behave

  Background:
  pass

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!


  Scenario: run a simple test _ 1
    Given we have behave installed
    When we implement a test <User>
    Then behave will test it for us!

  Scenario Outline: Blenders
    Given I put <thing> in a blender,
    When I switch the blender on
    Then it should transform into <other thing>

    Examples: Amphibians
      | thing         | other thing | another  |
      | Red Tree Frog | mush        | not used |

    Examples: Consumer Electronics
      | thing        | other thing |
      | iPhone       | toxic waste |
      | Galaxy Nexus | toxic waste |