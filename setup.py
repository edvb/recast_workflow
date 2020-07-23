from setuptools import setup

extras_require = {
    'cli': ['click', 'click_completion'],
}

extras_require['test'] = sorted(
    set(
        extras_require['cli']
        + ['pytest~=3.5']
    )
)

setup(extras_require=extras_require)
