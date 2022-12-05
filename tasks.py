from invoke import task

@task
def robot(ctx):
    ctx.run("robot src/tests", pty=True)