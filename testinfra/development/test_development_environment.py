import pytest


def test_development_app_dependencies(Package):
    """
    Ensure development apt dependencies are installed.
    """
    development_apt_dependencies = [
      'libssl-dev',
      'python-dev',
      'python-pip',
    ]
    for dependency in development_apt_dependencies:
        p = Package(dependency)
        assert p.is_installed


@pytest.mark.parametrize('pip_package,version', [
    ('Flask-Testing', '0.6.1'),
    ('Flask', '0.11.1'),
    ('Jinja2', '2.8'),
    ('MarkupSafe', '0.23'),
    ('Werkzeug', '0.11.11'),
    ('beautifulsoup4', '4.5.1'),
    ('click', '6.6'),
    ('coverage', '4.2'),
    ('first', '2.0.1'),
    ('funcsigs', '1.0.2'),
    ('itsdangerous', '0.24'),
    ('mock', '2.0.0'),
    ('pbr', '1.10.0'),
    ('pip-tools', '1.7.0'),
    ('py', '1.4.31'),
    ('pytest-cov', '2.4.0'),
    ('pytest', '3.0.3'),
    ('selenium', '2.53.6'),
    ('six', '1.10.0'),
])
def test_development_pip_dependencies(Command, pip_package, version):
    """
    Declare SecureDrop app pip requirements. On the development VM,
    the pip dependencies should be installed directly via pip, rather
    than relying on the deb packages with pip-wheel inclusions.
    Versions here are intentionally hardcoded to track changes.
    """
    c = Command('pip freeze')
    assert "{}=={}".format(pip_package, version) in c.stdout


def test_development_securedrop_env_var(File):
    """
    Ensure that the SECUREDROP_ENV var is set to "dev".


    TODO: this isn't really checking that the env var is set,
    just that it's declared in the bashrc. spec_helper ignores
    env vars via ssh by default, so start there.
    """

    f = File('/home/vagrant/.bashrc')
    assert f.is_file
    assert f.user == 'vagrant'
    assert f.contains('^export SECUREDROP_ENV=dev$')
