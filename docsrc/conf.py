from ablog.conf import *
from photon_platform.formulator import __version__

org = "photon-platform"
org_name = "PHOTON platform"

repo = "formulator"
repo_name = "Formulator"

blog_title = f"{org_name} • {repo_name}"
project = f"{org_name}<br/>•<br/>{repo_name}"
version = __version__
release = ""  # The full version, including alpha/beta/rc tags.

copyright = f"{year}, {org_name}"
author = org_name

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = f"https://{org}.github.io/{repo}"
html_base_url = blog_baseurl
html_baseurl = blog_baseurl

blog_authors = {
    "phi": ("phi ARCHITECT", None),
}

html_theme_options = {
    "logo": "logo.png",
    "logo_name": True,
    "github_user": org,
    "github_repo": repo,
    "github_button": True,
}
