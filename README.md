django-timing-test-runner
=========================

A test runner for django-jenkins that prints your 10 slowest tests.

## Requirements

Only [django-jenkins](https://github.com/kmmbvnr/django-jenkins). django-jenkins isn't just for Jenkins, it useful at the command line for running your tests every day.

    pip install django-jenkins
    OR
    pip install git+git://github.com/kmmbvnr/django-jenkins.git

## Usage

First setup django-jenkins so you can use the `jtest` command. Add these to your `settings.py`, changing _my_project_:

    INSTALLED_APPS += ('django_jenkins',)
    JENKINS_TASKS = ('django_jenkins.tasks.django_tests',)
    PROJECT_APPS = [appname for appname in INSTALLED_APPS if appname.startswith('my_project')]

Clone django-timing-test-runner:

    git clone https://github.com/grahamking/django-timing-test-runner.git

Copy `test_runner.py` into your project. Add it to your settings:

    JENKINS_TEST_RUNNER = 'myproj.apps.test_runner.TimeRunner'

Run it:

    manage jtest

After the tests finish, you should see a list of the ten slowest tests, with timings.
