# Frequenty Asked Questions

## I can't install recast-wf

If upon running `pip install ./recast_wf` give you an error such as `Command "python setup.py
egg_info" failed with error code 1` you can try the following commands to fix pip and the
installation tools:

```
pip install --upgrade setuptools
pip install --upgrade pip
pip install --upgrade distlib
```

## How do I fix a "permission denied" error?

If you are getting a permission denied error message when running yadage it is
mostly likely an issue with your user not being able to access docker images
without `sudo`.  To fix it you need to add your user to the docker group with:

```
sudo usermod -aG docker $USER
```

Then you need to log out and log back in so the changes to your user takes
effect. This should allow you to use docker without `sudo` or root, which is
required when running yadage. To test that it worked execute `docker run
hello-world` and you should get a `Hello from Docker!` followed by information
about docker.

## How do I fix a gcd error

If you are using python 3.9 or above you might run into the error `ImportError: cannot import name
'gcd' from 'fractions'`. This is because adage requires a older version of the library networkx
which uses the depreciated `fractions.gcd` instead of `math.gcd`. This can be solved by editing the
file given in the error message with `networkx/algorithms/dag.py` at the end and changing the first
or second line which has `from fractions import gcd` to `from math import gcd`.

## How do I fix a cannot remove error

If you see a error that reads `rm: cannont remove ./workdir/...: Persmision denined` then there
might be a problem were a docker from a previous created files as a root user. To solve this simply
run `sudo rm -rf workdir` to remove the old run with the root.
