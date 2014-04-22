ruby-rpm
========

Forked from imeyer's https://github.com/imeyer/ruby-1.9.3-rpm and updated ruby 2.0

## How to rpm packge build ##

### Running root ###


```
yum -y install ncurses ncurses-devel gdbm gdbm-devel glibc-devel autoconf gcc unzip openssl-devel db4-devel byacc bison readline readline-devel 
yum -y install gcc make rpm-build redhat-rpm-config rpmdevtools
adduser rpmbuild
su - rpmbuild
```

### Running rpmbuild user ####


```
rpmdev-setuptree
cd ~/rpmbuild
wget -O SPECS/ruby20.spec https://raw.githubusercontent.com/lesstif/ruby-rpm/master/ruby20.spec 
wget -O SOURCES/ruby-2.0.0-p451.tar.gz ftp://ftp.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p451.tar.gz
rpmbuild -bb SPECS/ruby20.spec 
```
