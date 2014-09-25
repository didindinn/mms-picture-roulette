#!/usr/bin/env python

import os

from roulette import app
from flask.ext.script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def runserver():
    app.run("0.0.0.0", port=5001)


if __name__ == '__main__':
    manager.run()
