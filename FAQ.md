# Frequenty Asked Questions

## Fix installation errors

If upon running `pip install ./recast_wf` give you an error such as `Command "python setup.py
egg_info" failed with error code 1` you can try the following commands to fix pip and the
installation tools

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

