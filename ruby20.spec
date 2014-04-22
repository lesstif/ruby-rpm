%global rubyxver        2.0
%global rubyver         2.0.0
%global patchlevel      p451

%{!?ruby_vendorlib:     %global ruby_vendorlib  %{_prefix}/lib/ruby}
%{!?ruby_vendorarch:    %global ruby_vendorarch %{_libdir}/ruby}
%{!?ruby_sitelib:       %global ruby_sitelib    %{ruby_vendorlib}/site_ruby}
%{!?ruby_sitearch:      %global ruby_sitearch   %{ruby_vendorarch}/site_ruby}

Name:           ruby
Version:        %{rubyver}%{patchlevel}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses ncurses-devel gdbm gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  autoconf gcc unzip openssl-devel db4-devel byacc
BuildRequires:  bison
BuildRequires:  readline readline-devel

Requires:       libyaml
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/${rubyxver}/ruby-%{rubyver}-%{patchlevel}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = %{rubyxver}
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: ruby(rubygems)
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.


%prep
%setup -n ruby-%{rubyver}-%{patchlevel}

%build
# bug 489990
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir} \
  --with-sitedir='%{ruby_sitelib}' \
  --with-sitearchdir='%{ruby_sitearch}' \
  --with-vendordir='%{ruby_vendorlib}' \
  --with-vendorarchdir='%{ruby_vendorarch}'

#make RUBY_INSTALL_NAME=ruby %{?_smp_mflags} COPY="cp -p" %{?_smp_mflags}
make %{?_smp_mflags}

%check
make test

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}
%doc %{_mandir}/man1/erb.1.gz
%doc %{_mandir}/man1/irb.1.gz
%doc %{_mandir}/man1/rake.1.gz
%doc %{_mandir}/man1/ri.1.gz
%doc %{_mandir}/man1/ruby.1.gz

%changelog
* Thu Apr 22 2014 KwangSeob Jeong <lesstif@gmail.com> - 2.0.0-p451
- Update for ruby 2.0.0-p451
* Thu Sep 19 2013 Daniel Haskin <djhaskin987@gmail.com> - 1.9.3-p448
- Added man pages entries
* Thu Jun 27 2013 Henrik <henrik@haf.se> - 1.9.3-p448
- Update for Ruby 1.9.3-p448 release.
* Thu May 23 2013 Attila Bogár <attila@fidescreativa.com> - 1.9.3-p429
- Update for Ruby 1.9.3-p429 release.
* Tue Apr 23 2013 Aleks Bunin <sbunin@gmail.com> - 1.9.3-p392
- Update for Ruby 1.9.3-p392 release.
* Thu Feb 14 2013 Martin Bokman <martin@bokman.org> - 1.9.3-p385
- Update for Ruby 1.9.3-p385 release.
* Tue Feb 5 2013 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p374
- Update for Ruby 1.9.3-p327 release.
* Sun Nov 25 2012 Gareth Jones <me@gazj.co.uk> - 1.9.3-p327
- Update for Ruby 1.9.3-p327 release.
* Wed Apr 25 2012 mathew <meta@pobox.com> - 1.9.3-p194-1
- Update for Ruby 1.9.3-p194 release.
* Sat Feb 24 2012 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p125-1
- Spec to replace system ruby with 1.9.3-p125
