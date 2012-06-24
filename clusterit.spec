Summary:	Collection of clustering tools
Summary(pl):	Kolekcja narz�dzi pomocnych przy tworzeniu klastr�w
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
ClusterIt to zbi�r oprogramowania umo�liwiaj�cego �atwe zarz�dzanie
du�ymi grupami maszyn. Nie dostarcza �rodowiska do programowania
r�wnoleg�ego, lecz ma s�u�y� do zarz�dzania takowym albo po prostu do
zarz�dzania du�ymi farmami serwer�w. Ma takie cechy jak r�wnoleg�e
rsh, r�wnoleg�e kopiowanie, r�wnoleg�e wirtualne xterminale (xtermy)
oraz u�atwienia do szeregowania zada� w celu przeprowadzania
r�wnoleg�ej kompilacji. Ma tak�e programy umo�liwiaj�ce synchronizacj�
w skryptach pow�oki.

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
