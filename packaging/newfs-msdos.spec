Name:       newfs-msdos
Summary:    newfs-msdos
Version:    1.0.0
Release:    1
Group:      System/Tool
License:    BSD-2-Clause
Source0:    %{name}-%{version}.tar.gz
Source1:    newfs-msdos.manifest

BuildRequires:  cmake

%description
newfs-msdos tool

%prep
%setup -q

%cmake .

%build
cp %{SOURCE1} .
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%manifest %{name}.manifest
%license LICENSE
%{_bindir}/newfs_msdos
