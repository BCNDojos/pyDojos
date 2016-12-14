from behave import *

from tamagotchi.object_oriented.src.lib.unitlimitedparameter import \
    UnitLimitedParameter
from tamagotchi.object_oriented.src.lib.usualdigestivesystem import \
    UsualDigestiveSystem
from tamagotchi.object_oriented.src.tamagotchi import Tamagotchi


def update_last_values(context):
    context.last_fullness = context.tamagotchi.fullness
    context.last_hungriness = context.tamagotchi.hungriness


# Given


@given('I have a Tamagotchi')
def step_having_tamagotchi(context):

    limited_param = UnitLimitedParameter(5, 10)

    digestive_sys = UsualDigestiveSystem(fullness=limited_param)

    tamagotchi = Tamagotchi(
        digestive_sys=digestive_sys
    )

    context.expected_diff = limited_param.difference
    context.tamagotchi = tamagotchi


# When


@when('I feed it')
def step_feed(context):
    update_last_values(context)
    context.tamagotchi.feed_it()


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
