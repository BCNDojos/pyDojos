from behave import *

from tamagotchi.object_oriented.src.lib.bodyenergy import BodyEnergy
from tamagotchi.object_oriented.src.lib.gameaddiction import GameAddiction
from tamagotchi.object_oriented.src.lib.unitlimitedparameter import \
    UnitLimitedParameter
from tamagotchi.object_oriented.src.lib.unitparameter import UnitParameter
from tamagotchi.object_oriented.src.lib.usualdigestivesystem import \
    UsualDigestiveSystem
from tamagotchi.object_oriented.src.tamagotchi import Tamagotchi


def update_last_values(context):
    context.last_fullness = context.tamagotchi.fullness
    context.last_hungriness = context.tamagotchi.hungriness
    context.last_happiness = context.tamagotchi.happiness
    context.last_tiredness = context.tamagotchi.tiredness


# Given


@given('I have a Tamagotchi')
def step_having_tamagotchi(context):

    param = UnitParameter(5)
    limited_param = UnitLimitedParameter(5, 10)

    addiction = GameAddiction(happiness=param)
    digestive_sys = UsualDigestiveSystem(fullness=limited_param)
    energy = BodyEnergy(fullness=limited_param)

    tamagotchi = Tamagotchi(
        addiction=addiction,
        digestive_sys=digestive_sys,
        energy=energy
    )

    context.expected_diff = limited_param.difference
    context.tamagotchi = tamagotchi


# When


@when('I feed it')
def step_feed(context):
    update_last_values(context)
    context.tamagotchi.feed_it()


@when('I play with it')
def step_play(context):
    update_last_values(context)
    context.tamagotchi.play_with_it()


@when('I put it to bed')
def step_put_to_bed(context):
    update_last_values(context)
    context.tamagotchi.put_to_bed()


@when('I make it poop')
def step_poop(context):
    update_last_values(context)
    context.tamagotchi.make_it_poop()


# Then


@then('its fullness is increased')
def step_fullness_should_increase(context):
    assert context.tamagotchi.fullness == context.last_fullness \
                                          + context.expected_diff


@then('its fullness is decreased')
def step_impl(context):
    assert context.tamagotchi.fullness == context.last_fullness \
                                          - context.expected_diff


@then('its hungriness is increased')
def step_hungry_should_increase(context):
    assert context.tamagotchi.hungriness == context.last_hungriness \
                                            + context.expected_diff


@then('its hungriness is decreased')
def step_hungry_should_decrease(context):
    assert context.tamagotchi.hungriness == context.last_hungriness \
                                            - context.expected_diff


@then('its happiness is increased')
def step_happy_should_increase(context):
    assert context.tamagotchi.happiness == context.last_happiness \
                                           + context.expected_diff


@then('its happiness is decreased')
def step_happy_should_decrease(context):
    assert context.tamagotchi.happiness == context.last_happiness \
                                           - context.expected_diff


@then('its tiredness is increased')
def step_tired_should_increase(context):
    assert context.tamagotchi.tiredness > context.last_tiredness


@then('its tiredness is decreased')
def step_tired_should_decrease(context):
    assert context.tamagotchi.tiredness < context.last_tiredness

