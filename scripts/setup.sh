#!/bin/bash
# Package Setup Script
def_name=$PACKAGE_NAME
def_github_username=$PACKAGE_GITHUB_USERNAME
def_author=$PACKAGE_AUTHOR
def_email=$PACKAGE_EMAIL
def_description="Python package template description"
def_keywords="python"

read -p "Enter package name [$def_name]: " name
name=${name:-$def_name}
read -p "Enter package path [$name]: " path
path=${path:-$name}
read -p "Enter package description [$def_description]: " description
description=${description:-$def_description}
read -p "Enter package keywords (comma separated) [$def_keywords]: " keywords
keywords=${keywords:-$def_keywords}

read -p "Enter author name [${def_author:-$(git config --get user.name)}]: " author
author=${author:-${def_author:-$(git config --get user.name)}}
read -p "Enter author email [${def_email:-$(git config --get user.email)}]: " email
email=${email:-${def_email:-$(git config --get user.email)}}

read -p "Enter github username [${def_github_username:-$author}]: " github_username
github_username=${github_username:-${def_github_username:-$author}}

echo ""
echo "Package information:"
echo "Name: $name"
echo "Description: $description"
echo "Keywords: $keywords"

echo "Github username: $github_username"
echo "Author: $author"
echo "Email: $email"
echo ""

read -p "Confirm changes? [Y/n] " confirm
confirm=${confirm:-Y}

if [ "$confirm" != "Y" ] && [ "$confirm" != "y" ]; then
    echo "Aborting."
    exit 0
fi

mv package_src "$path"

sed_opt=""
if [[ "$(uname)" == "Darwin" ]]; then
    sed_opt=("-i" "")
else
    sed_opt=("-i")
fi

sed "${sed_opt[@]}" "s/<package-name>/$name/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<package-path>/$path/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<github-username>/$github_username/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<author>/$author/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<email>/$email/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<description>/$description/g" setup.cfg README_TEMPLATE.md
sed "${sed_opt[@]}" "s/<keywords>/$keywords/g" setup.cfg README_TEMPLATE.md

title=$(echo $name| sed 's/-/\n/g' | awk '{print toupper(substr($0,1,1)) substr($0,2)}' | tr '\n' ' ')
sed "${sed_opt[@]}" "s/<Package-Name>/$title/g" README_TEMPLATE.md

mv README.md README_DELETE_ME.md
mv README_TEMPLATE.md README.md
echo -e "\033[32mDone.\033[0m Please remember to modify \033[31m'install_requires'\033[0m in \033[31m'setup.cfg'\033[0m."
