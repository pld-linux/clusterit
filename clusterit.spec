Summary:	Collection of clustering tools
Summary(pl):	Kolekcja narzêdzi pomocnych przy tworzeniu klastrów
Name:		clusterit
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications/Shells	
Source0:	http://www.garbled.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	f044f524d93b8644183b3847ca9a0752
URL:		http://www.garbled.net/clusterit.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClusterIt is a suite of software to allow easy maintenance of large
groups of machines. It does not provide a parallel programing
environment, but is meant to be utilized in managing one, or simply to
manage massive server farms. It includes such features as parallel
rsh, parallel copy, parallel virtual xterminals (xterms), and job
scheduling facilities for performing parallel compiling. It also has
programs to allow barrier syncing in shell scripts.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README README-DVT TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
