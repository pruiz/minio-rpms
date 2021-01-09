%define debug_package %{nil}

Name:          minio
Summary:       High performance object storage server compatible with Amazon S3 APIs
Version:       2021.01.08.211821
Release:       1%{?dist}
License:       ASL 2.0

Source0:       https://dl.min.io/server/minio/release/linux-amd64/archive/%{name}.RELEASE.%(echo %{version} | tr '.' '-' |sed -re 's/-(..)(..)(..)$/T\1-\2-\3Z/g')
Source3:       https://raw.githubusercontent.com/minio/minio/%{tag}/LICENSE
URL:           https://min.io
BuildRoot:     %{_tmppath}/%{name}-root

%description
The 100 percent Open Source, Enterprise-Grade,
Amazon S3 Compatible Object Storage

%prep

%build

%install
rm -rf %{buildroot}

install -p -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/certs/

# install binary
install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_sbindir}/%{name}

# license
cp %{SOURCE3} .

%clean
rm -rf %{buildroot}


%pre

%files
%defattr(-,root,root,-)
%{_sbindir}/*
%license LICENSE


%changelog
* Mon Jan 31 2020 Pablo Ruiz <pablo.ruiz@gmail.com> - 2020.01.25.030219-1
- Update to RELEASE.2020-01-25T02-50-51Z
