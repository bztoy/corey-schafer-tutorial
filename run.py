import basic
import advanced
import common_modules_n_packages
import mini_projects

# Switch
sw = {
    # Basic Package
    basic.key: False,
    advanced.key: True,
    common_modules_n_packages.key: False,
    mini_projects.key: False
}


def main():
    # Basic
    if sw[basic.key]:
        basic.run()

    # Advanced
    if sw[advanced.key]:
        advanced.run()

    # Common Modules and Packages
    if sw[common_modules_n_packages.key]:
        common_modules_n_packages.run()

    # Mini projects
    if sw[mini_projects.key]:
        mini_projects.run()


if __name__ == "__main__":
    main()
