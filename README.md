ruby-rpm
========

Forked from imeyer's https://github.com/imeyer/ruby-1.9.3-rpm and updated to ruby 2.0, 2.1, 2.2.

## How to rpm packge build ##

### Running root ###

```bash
yum -y install ncurses ncurses-devel gdbm gdbm-devel glibc-devel autoconf gcc
unzip openssl-devel db4-devel byacc bison readline readline-devel 
yum -y install gcc make rpm-build redhat-rpm-config rpmdevtools
adduser rpmbuild
su - rpmbuild
```

### Running rpmbuild user ####

#### Prerequisite

```sh
rpmdev-setuptree
cd ~/rpmbuild
```

#### ruby 2.1

```sh
wget -O SPECS/ruby-2.1.spec https://raw.githubusercontent.com/lesstif/ruby-rpm/master/ruby-2.1.spec 
wget -O SOURCES/ruby-2.1.8.tar.gz https://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.8.tar.gz
rpmbuild -bb SPECS/ruby-2.1.spec 
```

#### ruby 2.2 ####

```sh
wget -O SPECS/ruby-2.2.spec https://raw.githubusercontent.com/lesstif/ruby-rpm/master/ruby-2.2.spec 
wget -O SOURCES/ruby-2.2.4.tar.gz https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.4.tar.gz
rpmbuild -bb SPECS/ruby-2.2.spec 
```
