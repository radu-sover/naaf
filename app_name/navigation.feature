Feature: Navigation By left side Menu and URL

  @smoke
  Scenario: I open the Trainings page and navigate to Calendar
    Given I am on "TrainingsPage" page
    When I click on "btn_calendar" from "NavigationSection"
    Then I am at "CalendarPage" page

  @smoke
  Scenario: I open Calendar page and navigate to Trainings
    Given I am on "CalendarPage" page
    When I click on "btn_trainings" from "NavigationSection"
    Then I am at "TrainingsPage" page

  Scenario: I open the Trainings page
    Given I am on Trainings page

  Scenario: I open the wrong page
    Given I am on Calendar-tr page
