%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from rspec-expectations-2.5.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rspec-expectations
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: rspec-expectations-2.5.0
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 2.5.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/rspec/rspec-expectations
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
Requires: %{?ruby_dist_dash}rubygem(diff-lcs) >= 1.1.2
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
rspec expectations (should[_not] and matchers)


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 2.5.0-1.spec
- Rebuild for Ruby Enterprise Edition

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 2.5.0-1
- Initial package
