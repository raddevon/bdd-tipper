Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page

    Scenario: Calculate the tip amount at 20% for a $50 meal
        When I go to the tip calculator
        And I enter a <meal_cost> of "50"
        And I enter a <tip_percentage> of "20"
        And I click submit
        Then I should see a result of "$10.00"
