Summary:	Collection of clustering tools
Summary(pl.UTF-8):	Kolekcja narzędzi pomocnych przy tworzeniu klastrów
Name:		clusterit
Version:	2.5
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://www.garbled.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	f0e772e07122e388de629fb57f7237ab
URL:		http://www.garbled.net/clusterit.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClusterIt is a suite of software to allow easy maintenance of large
groups of machines. It does not provide a parallel programing
environment, but is meant to be utilized in managing one, or simply to
manage massive server farms. It includes such features as parallel
rsh, parallel copy, parallel virtual xterminals (xterms), and job
scheduling facilities for performing parallel compiling. It also has
programs to allow barrier syncing in shell scripts.

%description -l pl.UTF-8
ClusterIt to zbiór oprogramowania umożliwiającego łatwe zarządzanie
dużymi grupami maszyn. Nie dostarcza środowiska do programowania
równoległego, lecz ma służyć do zarządzania takowym albo po prostu do
zarządzania dużymi farmami serwerów. Ma takie cechy jak równoległe
rsh, równoległe kopiowanie, równoległe wirtualne xterminale (xtermy)
oraz ułatwienia do szeregowania zadań w celu przeprowadzania
równoległej kompilacji. Ma także programy umożliwiające synchronizację
w skryptach powłoki.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

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
%{_mandir}/man*/*
