# How to Download Multiple Files with Wget

If you want to download multiple files at once, use the `-i` option followed by the path to a local or external file containing a list of the URLs to be downloaded. 

Each URL needs to be on a separate line.

In the following example we are downloading the Arch Linux, Debian, and Fedora iso files with URLs specified in the linux-distros.txt file:

```wget -i linux-distros.txt```

By default, Wget will save the downloaded file in the current working directory. To save the file to a specific location, use the `-P` option:  

`wget -P /mnt/iso http://mirrors.mit.edu/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso`

