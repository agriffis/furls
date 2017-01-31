from __future__ import absolute_import, unicode_literals

import os
import pipes
import subprocess
import sys


def update_env(envbash, env=os.environ, missing_ok=False, remove=True):
    if missing_ok and not os.path.exists(envbash):
        return

    # run the script, then print the new environment in python repr
    inline = '''
        set -a
        source %s >/dev/null
        %s -c "import os; print(repr(dict(os.environ)))"
    ''' % (pipes.quote(envbash), pipes.quote(sys.executable))
    nenv = eval(subprocess.check_output(['bash', '-c', inline]))

    # update env, and remove any unset vars
    env.update(nenv)
    if remove:
        for k in set(env) - set(nenv):
            del env[k]
