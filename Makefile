unit:
    @nosetests -s --verbosity=2

deploy:
    @echo "Make sure you changed the version number if appropriate"
    python setup.py register sdist bdist_wininst upload

clean:
    @printf "Cleaning up files that are already in .gitignore... "
    @for pattern in `cat .gitignore`; do find . -name "$$pattern" -delete; done
    @echo "OK!"
