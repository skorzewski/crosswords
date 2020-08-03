#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

from tqdm import tqdm

import fire

# abcd
# efgh
# ijkl
# mnop

def crosswords(lexicon_file_name, start_from=0):
    with open(lexicon_file_name, 'r') as lexicon_file:
        lexicon = lexicon_file.read().splitlines()
    for abcd in tqdm(lexicon[start_from:]):
        a, b, c, d = tuple(abcd)
        letters = a + b + c + d
        re_aeim = re.compile(f'{a}[^{abcd}][^{abcd}][^{abcd}]')
        for aeim in filter(re_aeim.match, lexicon):
            _, e, i, m = tuple(aeim)
            re_efgh = re.compile(f'{e}[^{abcd}{e}{i}{m}][^{abcd}{e}{i}{m}][^{abcd}{e}{i}{m}]')
            for efgh in filter(re_efgh.match, lexicon):
                _, f, g, h = tuple(efgh)
                re_bfjn = re.compile(f'{b}{f}[^{abcd}{efgh}{i}{m}][^{abcd}{efgh}{i}{m}]')
                for bfjn in filter(re_bfjn.match, lexicon):
                    _, _, j, n = tuple(bfjn)
                    re_ijkl = re.compile(f'{i}{j}[^{abcd}{efgh}{i}{j}{m}{n}][^{abcd}{efgh}{i}{j}{m}{n}]')
                    for ijkl in filter(re_ijkl.match, lexicon):
                        _, _, k, l = tuple(ijkl)
                        re_cgko = re.compile(f'{c}{g}{k}[^{abcd}{efgh}{ijkl}{m}{n}]')
                        for cgko in filter(re_cgko.match, lexicon):
                            o = cgko[3]
                            re_mnop = re.compile(f'{m}{n}{o}[^{abcd}{efgh}{ijkl}{m}{n}{o}]')
                            for mnop in filter(re_mnop.match, lexicon):
                                p = mnop[3]
                                dhlp = d + h + l + p
                                if dhlp in lexicon:
                                    print(f'{abcd}\n{efgh}\n{ijkl}\n{mnop}\n'.upper())
            


if __name__ == '__main__':
    fire.Fire(crosswords)
