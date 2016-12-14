Feature: Playing with Tamagotchi
  As a Tamagotchi owner
  I want to play with my Tamagotchi
  So that I can make it happier
  Scenario: Simple action
  Given I have a Tamagotchi
  When I play with it
  Then its happiness is increased
  And its tiredness is increased