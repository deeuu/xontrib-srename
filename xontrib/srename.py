def _init():

    from argparse import ArgumentParser
    import os
    import re

    def _parse_srename_args(args):
        parser = ArgumentParser(prog='srename')
        parser.add_argument(
            'pattern',
            help="Pattern to evaluate on a file name"
        )
        parser.add_argument(
            'replacement',
            help="String or function to replace matched content defined by PATTERN"
        )
        parser.add_argument(
            'files',
            nargs='+',
            help="Files to rename"
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help="Do not rename files")
        parser.add_argument(
            '--invert',
            action='store_true',
            help="Reverse the order or PATTERN and REPLACEMENT"
        )
        args = parser.parse_args(args)
        return args

    def _srename(args):

        args = _parse_srename_args(args)
        pattern, replacement = args.pattern, args.replacement

        if args.invert:
            pattern, replacement = replacement, pattern

        for old_name in args.files:
            if not os.path.exists(old_name):
                print(f'Warning: {old_name} does not exist')
                continue

            if not os.path.isfile(old_name):
                print(f'Warning: {old_name} is not a file')
                continue

            new_name = os.path.join(
                os.path.dirname(old_name),
                re.sub(pattern, replacement, os.path.basename(old_name))
            )

            if (old_name == new_name):
                continue

            if os.path.exists(new_name):
                print(f'Warning: {new_name} already exists')
                continue

            if args.dry_run:
                print(f'Info: {old_name} → {new_name} (not renaming as dry run)')
            else:
                os.rename(old_name, new_name)

    return _srename


aliases['srename'] = _init()