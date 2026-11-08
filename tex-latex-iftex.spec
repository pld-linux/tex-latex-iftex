Summary:	IfTeX – Am I running under pdfTeX, XeTeX or LuaTeX?
Name:		tex-latex-iftex
Version:	1.0g
Release:	2
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	https://mirrors.ctan.org/macros/generic/iftex.zip
# Source0-md5:	dc13cf5c8c0b48ab91b0c2bb6144bd28
URL:		https://ctan.org/pkg/iftex/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
Provides:	tex(iftex.sty)
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package, which works both for Plain TeX and for LaTeX, defines the
\ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for testing which
engine is being used for typesetting.

The package also provides the \RequirePDFTeX, \RequireXeTeX, and
\RequireLuaTeX commands which throw an error if pdfTeX, XeTeX or
LuaTeX (respectively) is not the engine in use.

%prep
%setup -q -n iftex

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/iftex

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/iftex
cp -p *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/iftex

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README.md
%doc %{_datadir}/texmf/doc/latex/iftex
%{_datadir}/texmf/tex/latex/iftex
