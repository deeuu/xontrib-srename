def _init():

    from argparse import ArgumentParser
    import pathlib
    from shutil import copyfile
    import os
    import re

    def _parse_srename_args(args):
        parser = ArgumentParser(prog='srename')
        parser.add_argument(
            'pattern',
            help="Pattern to evaluate on a file name",
        )
        parser.add_argument(
            'replacement',
            help="String or function to replace matched content defined by PATTERN",
        )
        parser.add_argument(
            'paths',
            nargs='+',
            help="Path(s) to rename",
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help="Do not rename files"
        )
        parser.add_argument(
            '--copy',
            action='store_true',
            help="Copy files, rather than move existing"
        )
        parser.add_argument(
            '--dest',
            type=str,
            help="Path to move/copy the renamed files to"
        )
        parser.add_argument(
            '--include-dirs',
            action='store_true',
            help="Rename directories as well as files"
        )

        args = parser.parse_args(args)
        return args

    def _srename(args):

        args = _parse_srename_args(args)

        if args.dest and not os.path.isdir(args.dest):
            raise IOError(f'{args.dest} is not a directory')

        pattern, replacement = args.pattern, args.replacement

        paths = set([pathlib.Path(_).absolute().resolve() for _ in args.paths])
        if not args.include_dirs:
            paths = filter(lambda p: p.is_file(), paths)

        for old_name in sorted(paths, reverse=True):
            if not old_name.exists():
                print(f'Warning: {old_name} does not exist')
                continue

            new_name = old_name.parent / re.sub(pattern,
                                                replacement,
                                                old_name.name)

            if args.dest:
                new_name = pathlib.Path(args.dest) / new_name.name

            if (old_name == new_name):
                continue

            if new_name.exists():
                print(f'Warning: {new_name} already exists')
                continue

            if args.dry_run:
                print(f'Info: {old_name} → {new_name} (not renaming as dry run)')
            elif args.copy:
                copyfile(old_name, new_name)
            else:
                old_name.rename(new_name)

    return _srename


aliases['srename'] = _init()
