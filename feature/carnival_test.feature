Feature: US1: As a user I want to search cruises to The Bahamas with duration
between 6 and 9 days so that I will visualize all the options to choose
one. Right now, I don’t care about departure port.
Acceptance Criteria:
  1. A set of results will be displayed, default view will be a grid
  2. The user will be able to filter by price, using the slider bar
  3. The user will be able to sort by price, default value will be
  cheapest first

  US2: As a user I want to choose one sail and learn more about the trip,
  so that I will get more info about itinerary
  Acceptance Criteria:
  1. The itinerary page will be load
  2. The user will be able to read ABOUT each day
  3. A BOOK NOW button will be placed into the page


  Background:
    Given I am on carnival Home page

  Scenario: Search for a cruise
    Given I want to search for a cruise
    When I select "The Bahamas"
    And I select the duration
    Then The results are displayed on a grid

  Scenario: Filter by price
    Given I want to search for a cruise
    And I select "The Bahamas"
    And I select the duration
    When I Filter by price
    Then The results are shown according to the price rage
