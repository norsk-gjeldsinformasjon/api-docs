# Norsk Gjeldsinformasjon API documentation

Please report any issues using [GitHub issues](https://github.com/norsk-gjeldsinformasjon/api-docs/issues).
[PRs](https://github.com/norsk-gjeldsinformasjon/api-docs/issues) are also welcome.

Migration of the public documentation is currently a work in progress,
the old unmigrated documentation can be found
[on confluence](https://norskgjeld.atlassian.net/wiki/spaces/GJEL/overview)

# GitHub pages

Visit https://norsk-gjeldsinformasjon.github.io/api-docs/

# Local development

    python -m venv env # or: virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    mkdocs serve

## Adding mkdocs menu items

Because we want to control the order of menu items (left side menu), the menu
is defined in `mkdocs.yml`. When adding a new page, it should also be added
to where it belongs in this file.
