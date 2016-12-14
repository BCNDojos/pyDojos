Feature: Changing Tamagotchi Needs Over Time
  As a Tamagotchi owner
  I want my Tamagotchi's needs to change over time
  So that I have to look after it carefully
  Scenario: Time passing
  Given I have a Tamagotchi
  When time passes
  Then its tiredness is increased
  And its hungriness is increased
  And its happiness is decreased