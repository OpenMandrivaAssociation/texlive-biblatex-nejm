Name:		texlive-biblatex-nejm
Version:	49839
Release:	2
Summary:	Biblatex style for the New England Journal of Medicine (NEJM)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-nejm
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nejm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nejm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a biblatex numeric style based on the design of the New
England Journal of Medicine (NEJM).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-nejm/nejm.bbx
%{_texmfdistdir}/tex/latex/biblatex-nejm/nejm.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-nejm/README
%doc %{_texmfdistdir}/doc/latex/biblatex-nejm/biblatex-nejm.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-nejm/biblatex-nejm.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
