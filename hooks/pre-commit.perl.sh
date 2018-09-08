#!/usr/bin/env bash

if git rev-parse --verify HEAD >/dev/null 2>&1; then
    against=HEAD
else
    # Initial commit: diff against an empty tree object
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

# If there are whitespace errors, print the offending file names and fail.
git diff-index --check --cached $against --

# perl sample
git diff --cached --name-status | while read st file; do
    # skip deleted files
    if [ "$st" == 'D' ]; then continue; fi
    # do a check only on the perl files
    if [[ "$file" =~ "\.p[ml]$" ]] && ! perl -c "$file"; then
        echo "Perl syntax check failed for file: $file"
        exit 1
    fi
done
