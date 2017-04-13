Feature: Calendar and Trainings planning

  @smoke
  Scenario: I open dynamic page
    Given I am on "CalendarPage" page
    When  I click on "btn_plan_training" from "CalendarPage"
    And I wait for 1 seconds
    Then I am at "PlanTrainingPage" page
