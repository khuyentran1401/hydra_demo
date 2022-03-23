pip: install_format_packages download_config add_precommit install_git_hooks
poetry: poetry_install_format_packages download_config add_precommit install_git_hooks
pip_install_format_packages:
	pip install pre-commit commitizen

poetry_install_format_packages:
	poetry add -D pre-commit commitizen 

download_config:
	wget -O .flake8 https://gist.githubusercontent.com/khuyentran1401/f4a4c822320a9db266ad935b501be66e/raw/3ebf2b029490a970591caa733dd9d2e9767b184e/.flake8
	wget -O .pre-commit-config.yaml https://gist.githubusercontent.com/khuyentran1401/2d6fc241f6738fdc0946e62e1597223e/raw/8978d46db7b55d79c7b9823018d975efcf6a6184/.pre-commit-config.yaml

add_precommit:
	wget -O precommit https://gist.githubusercontent.com/khuyentran1401/b86812c900110c5cf4450e183669ae48/raw/55041856a74a27245f4273040516690c856a3f0a/pyproject.toml
	touch pyproject.toml 
	cat precommit >> pyproject.toml    
	rm precommit    

install_git_hooks:   
	pre-commit install      