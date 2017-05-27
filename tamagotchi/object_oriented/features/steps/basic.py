from behave import *
from nose.tools import assert_equal

from tamagotchi.object_oriented.src.lib.bodyenergy import BodyEnergy
from tamagotchi.object_oriented.src.lib.gameaddiction import GameAddiction
from tamagotchi.object_oriented.src.lib.unitlimitedparameter import \
    UnitLimitedParameter
from tamagotchi.object_oriented.src.lib.unitparameter import UnitParameter
from tamagotchi.object_oriented.src.lib.usualdigestivesystem import \
    UsualDigestiveSystem
from tamagotchi.object_oriented.src.tamagotchi import Tamagotchi


# Helpers


def update_description(context, prefix):
    context.description = '{!s}\n{!s} {!s}'.format(
        context.description,
        prefix,
        context.step.name
    )


def update_last_values(context):
    context.last_fullness = context.tamagotchi.fullness
    context.last_hungriness = context.tamagotchi.hungriness
    context.last_happiness = context.tamagotchi.happiness
    context.last_tiredness = context.tamagotchi.tiredness


# Given


@given('I have a Tamagotchi')
def step_having_tamagotchi(context):
    update_description(context, 'Given')

    game_param = UnitParameter(5)
    digestive_param = UnitLimitedParameter(5, 10)
    energy_param = UnitLimitedParameter(5, 10)

    addiction = GameAddiction(happiness=game_param)
    digestive_sys = UsualDigestiveSystem(fullness=digestive_param)
    energy = BodyEnergy(fullness=energy_param)

    tamagotchi = Tamagotchi(
        addiction=addiction,
        digestive_sys=digestive_sys,
        energy=energy
    )

    context.game_diff = game_param.difference
    context.digestive_diff = digestive_param.difference
    context.energy_diff = energy_param.difference
    context.tamagotchi = tamagotchi


# When


@when('I feed it')
def step_feed(context):
    update_description(context, 'When')
    update_last_values(context)
    context.tamagotchi.feed_it()


@when('I play with it')
def step_play(context):
    update_description(context, 'When')
    update_last_values(context)
    context.tamagotchi.play_with_it()


@when('I put it to bed')
def step_put_to_bed(context):
    update_description(context, 'When')
    update_last_values(context)
    context.tamagotchi.put_to_bed()


@when('I make it poop')
def step_poop(context):
    update_description(context, 'When')
    update_last_values(context)
    context.tamagotchi.make_it_poop()


@when('time passes')
def step_time_passes(context):
    update_description(context, 'When')
    update_last_values(context)
    context.tamagotchi.time_passes()


# Then


@then('its {parameter} is {change}')
def step_parameter_change(context, parameter, change):
    update_description(context, 'Then')

    if change == 'increased':
        diff_sign = 1
    elif change == 'decreased':
        diff_sign = -1
    else:
        raise ValueError('Change "{!s}" is not implemented'.format(change))

    if parameter == 'fullness':
        assert_equal(
            context.tamagotchi.fullness,
            context.last_fullness + context.digestive_diff * diff_sign,
            context.description
        )
    elif parameter == 'hungriness':
        assert_equal(
            context.tamagotchi.hungriness,
            context.last_hungriness + context.digestive_diff * diff_sign,
            context.description
        )
    elif parameter == 'happiness':
        assert_equal(
            context.tamagotchi.happiness,
            context.last_happiness + context.game_diff * diff_sign,
            context.description
        )
    elif parameter == 'tiredness':
        assert_equal(
            context.tamagotchi.tiredness,
            context.last_tiredness + context.energy_diff * diff_sign,
            context.description
        )
    else:
        raise ValueError('Parameter "{!s}" is not implemented'.format(parameter))
