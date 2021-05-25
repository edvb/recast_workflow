#!/usr/bin/env python
import argparse
import subprocess
import shlex


def runpythia(inputlhe, outputhepmc, nevents, pythiacard):
    if pythiacard is None or pythiacard == "default" or pythiacard == "null":
        pythiacard = 'pythia.tmpl'
    runcardname = 'pythia_card.dat'
    with open(pythiacard, 'r') as template:
        with open(runcardname, 'w+') as filled:
            filled.write(template.read().format(
                LHEF=inputlhe, NEVENTS=nevents))
    subprocess.check_call(shlex.split(
        './pythia8/examples/main42 {} {}'.format(runcardname, outputhepmc)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Steer pythia8.')
    parser.add_argument('inputlhe', help='Path to input LHE file.')
    parser.add_argument('outputhepmc', help='Path to output hepmc file.')
    parser.add_argument('nevents', help='number of events.')
    parser.add_argument('pythiacard', help='Optional path to card to run pythia with.', nargs='?', default='pythia.tmpl')
    args = parser.parse_args()
    runpythia(args.inputlhe, args.outputhepmc, args.nevents, args.pythiacard)
