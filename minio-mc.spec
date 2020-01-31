%define debug_package %{nil}

%define  tag   RELEASE.2020-01-25T03-02-19Z
%define  stag  %(echo "%{tag}" | sed -r -e 's/^RELEASE.//g' -e 's/(....)-(..)-(..)T(..)-(..)-(..)Z/\1.\2.\3.\4\5\6/g' )

Name:          minio-mc
Summary:       MinIO Client
Version:       %{stag}
Release:       1%{?dist}
License:       ASL 2.0

Source0:       https://dl.min.io/client/mc/release/linux-amd64/archive/mc.%{tag}
Source1:       https://raw.githubusercontent.com/minio/mc/%{tag}/LICENSE
URL:           https://min.io
BuildRoot:     %{_tmppath}/%{name}-root


%description
MinIO Client is a replacement for ls, cp, mkdir, diff and rsync commands for
filesystems and object storage.


%prep

%build

%install
rm -rf %{buildroot}

# install binary
install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE1} .


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%license LICENSE


%changelog
* Mon Jan 31 2020 Pablo Ruiz <pablo.ruiz@gmail.com> - 2020.01.25.030219-1
- Update to RELEASE.2020-01-25T03-02-19Z

