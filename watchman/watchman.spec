Name:           watchman
Version: 4.5.0
Release:        1%{?dist}
Summary:        Watches files and takes action when they change
License:        ASL 2.0
URL:            https://github.com/facebook/watchman/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  pcre-devel
BuildRequires:  python2-devel


%description
Watchman exists to watch files and record when they actually change. It
can also trigger actions (such as rebuilding assets) when matching files
change.


%prep
%autosetup


%build
./autogen.sh
%configure \
   --enable-stack-protector \
   --disable-statedir \
   --with-pcre \
   --with-python \
   --with-buildinfo="%{version}-%{release}"
%__make


%install
%make_install

# Generate the manpage with help2man
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/watchman -N > %{buildroot}/%{_mandir}/man1/%{name}.1

# We include README.markdown in %%doc below, and this installs in the
# wrong place anyway.
rm -rf %{buildroot}/%{_docdir}/%{name}-*


%files
%license LICENSE
%doc README.markdown
%{_bindir}/watchman*
%{_mandir}/man1/%{name}.1*
%{_libdir}/python2.7/site-packages/pywatchman
%{_libdir}/python2.7/site-packages/pywatchman-1.3.0-py2.7.egg-info


%changelog
