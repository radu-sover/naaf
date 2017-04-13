@smoke
Feature: Trainings management CRUD

  Background: Start from TrainingsPage
    Given I am on "TrainingsPage" page

  Scenario: I add new Training
    When I click on "btn_new_training" from "TrainingsPage"
    And I type "NAAF-TestAutomation" in "text_name" from "AddEditTrainingPage"
    And I type "NAAF-Description" in "text_description" from "AddEditTrainingPage"
    And I select "Technical" in "select_category" from "AddEditTrainingPage"
    And I type "2" in "text_modules" from "AddEditTrainingPage"
    And I type "4" in "text_duration" from "AddEditTrainingPage"
    And I select "Active" in "select_status" from "AddEditTrainingPage"
    And I click on "btn_save" from "AddEditTrainingPage"
    And I type "NAAF" in "text_filter_name" from "TrainingsPage"
    Then I see the "NAAF-TestAutomation" in "list_trainings" from "TrainingsPage"

  Scenario: I check for added Training with ng-repeat
    When I type "NAAF" in "text_filter_name" from "TrainingsPage"
    Then I see the "NAAF-TestAutomation" in "list_trainings" from "TrainingsPage"

  Scenario: I edit added Training
    When I type "NAAF-TestAutomation" in "text_filter_name" from "TrainingsPage"
    And I click on "btn_edit" for "NAAF-TestAutomation" training from "TrainingsPage"
    And I wait for 1 seconds
    Then I am at "AddEditTrainingPage" page

  Scenario: I delete added Training
    When I type "NAAF-TestAutomation" in "text_filter_name" from "TrainingsPage"
    And I click on "btn_delete" for "NAAF-TestAutomation" training from "TrainingsPage"
    And I click on "btn_delete" from "DeleteTrainingPage"
    And I type "NAAF-TestAutomation" in "text_filter_name" from "TrainingsPage"
    Then I do not see the "NAAF-TestAutomation" in "list_trainings" from "TrainingsPage"
    