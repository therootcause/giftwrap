# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014, John Dewey
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import subprocess

from git import Repo
import giturlparse

from giftwrap import log

LOG = log.get_logger()


def execute(command, cwd=None):
    """
    Executes a command in a subprocess.  Returns a tuple of
    (exitcode, out, err).

    :param command: Command string to execute.
    :param cwd: Directory to execute from.
    """

    original_dir = None
    if cwd:
        original_dir = os.getcwd()
        os.chdir(cwd)
        LOG.debug("Changed directory to %s", cwd)

    LOG.info("Running: '%s'", command)
    process = subprocess.Popen(command,
                               cwd=os.getcwd(),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True)
    (out, err) = process.communicate()
    exitcode = process.wait()

    LOG.debug("Command exitted with rc: %s; STDOUT: %s; STDERR: %s" %
              (exitcode, out, err))

    if cwd:
        os.chdir(original_dir)
        LOG.debug("Changed directory back to %s", original_dir)

    return exitcode, out, err


def clone_git_repo(repo, checkout_dir):
    parsedrepo = giturlparse.parse(repo, False)
    directory = os.path.join(checkout_dir, parsedrepo.repo)
    if not os.path.isdir(directory):
        Repo.clone_from(repo, directory)

    return directory
