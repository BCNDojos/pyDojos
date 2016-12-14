Feature: Feeding Tamagotchi
  As a Tamagotchi owner
  I want to feed my Tamagotchi
  So that I can satiate its hungriness
  Scenario: Simple action
  Given I have a Tamagotchi
  When I feed it
  Then its hungriness is decreased
  And its fullness is increased