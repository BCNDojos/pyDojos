def before_all(context):
    context.description = ""


def before_step(context, step):
    context.step = step
