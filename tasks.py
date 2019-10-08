from invoke import task
import os
import shutil

@task
def clean(ctx):
   shutil.rmtree("./build")
   shutil.rmtree("./dist")

@task
def pack(ctx):
   os.system("python setup.py sdist bdist_wheel --universal")

@task()
def install(ctx):
   os.system("pip install ./dist/robotframework_HippoDevLibrary_dev-0.0.1.dev1-py2.py3-none-any.whl")

@task()
def uninstall(ctx):
   os.system("pip uninstall robotframework-HippoDevLibrary-dev")

@task()
def reinstall(ctx):
    clean(ctx)
    pack(ctx)
    uninstall(ctx)
    install(ctx)

