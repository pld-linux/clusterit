Summary:	Collection of clustering tools
Summary(pl):	Kolekcja narzêdzi pomocnych przy tworzeniu klastrów
Name:		clusterit
Version:	2.3.1
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://www.garbled.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	4edea7bb3f1f2ffd12dcb62b94bd46ba
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

%description -l pl
ClusterIt to zbiór oprogramowania umo¿liwiaj±cego ³atwe zarz±dzanie
du¿ymi grupami maszyn. Nie dostarcza ¶rodowiska do programowania
równoleg³ego, lecz ma s³u¿yæ do zarz±dzania takowym albo po prostu do
zarz±dzania du¿ymi farmami serwerów. Ma takie cechy jak równoleg³e
rsh, równoleg³e kopiowanie, równoleg³e wirtualne xterminale (xtermy)
oraz u³atwienia do szeregowania zadañ w celu przeprowadzania
równoleg³ej kompilacji. Ma tak¿e programy umo¿liwiaj±ce synchronizacjê
w skryptach pow³oki.

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
%{_mandir}/man*/*
