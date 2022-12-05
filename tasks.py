from invoke import task

@task
def start(ctx):
    ctx.run("flask run src", pty=True)

@task
def robot(ctx):
    ctx.run("robot src/tests", pty=True)
