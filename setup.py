from setuptools import setup

extras_require = {
    'shellcomplete': ['click_completion'],
}

extras_require['test'] = sorted(
    set(
        extras_require['shellcomplete']
        + ['pytest~=3.5']
    )
)

setup(extras_require=extras_require)
