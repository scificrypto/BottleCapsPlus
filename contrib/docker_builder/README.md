# Dockerfile for building bottlecapsplus binaries.

Now, you can build your own bottlecapsplus files on all systems with docker and do it easy without installing depends on your system.

## How:

### Build docker image

```
sudo docker build .
```

### Run docker container

Builder will return HASH of image
Example:
Successfully built 9bbff825d50f

```
sudo docker run -it -v ~/path/to/bottlecapsplus/folder:/bottlecapsplus 9bbff825d50f
```

If your system uses SELINUX you may use --privileged=true key

```
sudo docker run --privileged=true -it -v ~/development/bottlecapsplus:/bottlecapsplus 9bbff825d50f
```

See bottlecapsplus-qt file in used bottlecapsplus folder and bottlecapsplusd file in src subfolder.