#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
import yaml
import zipfile
from pathlib import Path
import json


def parse_dfa(root):
    aut, = root.iter("automaton")
    start_state = None
    accepted_states = []
    edges = []
    for entry in aut:
        if entry.tag == 'state':
            if entry.find('initial') is not None:
                assert start_state is None
                start_state = entry.attrib['id']
            if entry.find('final') is not None:
                accepted_states.append(entry.attrib['id'])
        elif entry.tag == 'transition':
            edges.append(
                dict(
                    src=entry.find('from').text,
                    dst=entry.find('to').text,
                    char=entry.find('read').text,
                )
            )
    assert start_state is not None
    return dict(
        start_state=start_state,
        accepted_states=accepted_states,
        edges=edges
    )


def parse_pda(root):
    aut, = root.iter("automaton")
    start_state = None
    accepted_states = []
    edges = []
    for entry in aut:
        if entry.tag == 'state':
            if entry.find('initial') is not None:
                assert start_state is None
                start_state = entry.attrib['id']
            if entry.find('final') is not None:
                accepted_states.append(entry.attrib['id'])
        elif entry.tag == 'transition':
            src = entry.find('from').text
            dst = entry.find('to').text
            char = entry.find('read').text
            pop = entry.find('pop').text
            push = entry.find('push').text
            new_entry = {
                'src': src,
                'dst': dst,
                'char': char,
                'pop': pop,
                'push': push
            }
            edges.append(new_entry)

    assert start_state is not None
    return dict(
        start_state=start_state,
        accepted_states=accepted_states,
        edges=edges
    )


def parse_zip(zf, pda=False):
    if pda:
        for fname in zf.infolist():
            if not fname.is_dir() and fname.filename.endswith('.jff'):
                root = ET.fromstring(zf.read(fname))
                yield fname.filename, parse_pda(root)
    else:
        for fname in zf.infolist():
            if not fname.is_dir() and fname.filename.endswith('.jff'):
                root = ET.fromstring(zf.read(fname))
                yield fname.filename, parse_dfa(root)


def load_from_zip(filename, pda=False):
    with zipfile.ZipFile(filename, "r") as zf:
        return dict((Path(p).stem, dfa) for p, dfa in parse_zip(zf))


def load_from_list(filenames, pda=False):
    result = dict()
    if pda:
        for filename in filenames:
            result[Path(filename).stem] = parse_pda(
                ET.parse(filename).getroot())
    else:
        for filename in filenames:
            result[Path(filename).stem] = parse_dfa(
                ET.parse(filename).getroot())
    return result


def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    # add flags to parse from dfa or pda
    parser.add_argument('--pda', action='store_true',
                        help='parse from pda')
    parser.add_argument("-o",
                        dest="output",
                        nargs='?',
                        help="output file",
                        type=argparse.FileType('w'),
                        default=sys.stdout
                        )
    parser.add_argument("-j", dest="json", action="store_true")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-z',
                       dest="from_zip",
                       metavar="FILE_ZIP",
                       help="Create a YAML file from a ZIP file."
                       )
    group.add_argument('-f',
                       dest="from_files",
                       metavar='FILE_JFF',
                       nargs="+",
                       help="Create a YAML file from multiple JFLAP files."
                       )
    # print out a help message if no arguments are given or if the -h flag is used
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    if args.from_zip is not None:
        data = load_from_zip(args.from_zip, pda=args.pda)
    else:
        data = load_from_list(args.from_files, pda=args.pda)
    if args.json:
        json.dump(data, args.output)
    else:

        for key, value in sorted(data.items()):
            args.output.write(key + ":\n")
            args.output.write(
                "  start_state: " + "q" + str(value['start_state']) + "\n")
            # put all the accepted states in a list separated by commas
            args.output.write("  accepted_states: [")
            for i in range(len(value['accepted_states'])):
                if i == len(value['accepted_states']) - 1:
                    args.output.write("q" + str(value['accepted_states'][i]))
                else:
                    args.output.write(
                        "q" + str(value['accepted_states'][i]) + ", ")
            args.output.write("]\n")
            args.output.write("  edges:\n")
            for edge in sorted(value['edges'],
                               key=lambda x: (int(x['src']), int(x['dst']))):
                args.output.write("    - {src: " + "q" + str(
                    edge['src']) + ", dst: " + "q" + str(edge['dst']))
                if edge['char'] is not None:
                    args.output.write(", char: " + edge['char'])
                if edge['pop'] is not None:
                    args.output.write(", pop: " + edge['pop'])
                if edge['push'] is not None:
                    args.output.write(", push: " + edge['push'])
                args.output.write("}\n")
            args.output.write("\n")


if __name__ == '__main__':
    main()

# yaml.dump(parse_dfa('ex1.jff'), sys.stdout)
