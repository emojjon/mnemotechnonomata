#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:12:07 2021

@author: johan
"""

import random

adjectives = ("abnormal", "abusive", "adulterous", "affectionate", "alcoholic",
              "alluring", "anchimeric", "angry", "apomictic", "appealing", "appetizing", "arrogant",
              "astute", "at-the-ready", "attentive", "attractive", "barmy", "bat-shit-crazy", "batty",
              "bearded", "bedlam", "berserk", "blathering", "blithering",
              "bonkers", "bughouse", "bull-headed", "captivating", "circumcised", "cocky",
              "confused", "coockoo-for-coacoa-puffs", "costumed", "cowardly",
              "cracked", "cranky", "crawly", "crazed", "cruel-hearted",
              "cuckoo", "daffy", "daft", "dead", "deep", "delirious",
              "demanding", "demented", "deranged", "desirable", "dingy", "dippy",
              "disgusting", "disrespectful", "distraught", "disturbing",
              "domesticated", "drunken", "duck-like", "eccentric",
              "embarrassed-to-the-bone", "enamoured", "energetic", "engaging", "enticing", "erratic", "fascinating", "fay", "fear-inspiring",
              "fershnickered", "fetching", "feverish", "fiercely-loyal", "fighting", "filthy",
              "flabbergasted", "flaky", "flickering", "flipped", "flippedout",
              "flirting", "fluffy", "flummoxed", "freakedout", "free-loading",
              "frisky", "frozen", "fruity", "gaga", "gibbous", "godawful",
              "goofy", "goy", "greedy", "happy", "hairless", "harsh", "hateful",
              "haunting", "hideous", "high-end", "hilarious", "hot",
              "house-broken", "hyperactive", "idiotic", "illoyal",
              "impertinent", "impressive", "indecent", "infuriating",
              "insane", "insanely-creepy", "insecure", "internet-worthy",
              "intrepid", "kooky", "kosher", "legless", "leprous", "loco",
              "loony", "lugubrious", "lumpy", "lunatic", "mad", "magical",
              "maniacal", "massive", "medicated", "mental",
              "mentally-impaired", "metal", "mischievous", "misunderstood",
              "mogadored", "moonstruck", "naked", "narrow-minded", "niggardly",
              "nighttime", "nuts", "nutty", "nutty-as-a-fruitcake",
              "offensive", "outnumbered", "out-of-control", "outrageous",
              "out-to-lunch", "painfully-honest", "pea-brained", "peculiar",
              "pernickety", "perspicacious", "potty", "precocious", "prepossessing", "psycho",
              "psychotic", "quirky", "rebellious", "ridibund",
              "round-the-bend", "sadistic", "sanguine", "scatty", "schizo",
              "screwball", "screwy", "seductive", "self-absorbed", "self-centered",
              "senseless", "sexy", "shaky", "shivering", "sick", "sickened",
              "silly", "sinister", "slap-happy", "slimy", "slippery", "smarmy",
              "smelly", "speedy", "spicy", "startled", "startling", "steatopygous",
              "sticky", "stubborn", "swollen", "talking", "tempting", "territorial",
              "touched", "treyf", "tripping", "twisted", "unbalanced",
              "underhanded", "unglued", "ungodly", "unhinged", "unholy",
              "unstable", "unzipped", "up-to-no-good", "useless", "vengeful",
              "very-tactful", "vile", "violent", "wacky", "weird", "wild",
              "xeric", "yapping", "zippy", "zombie-like", )

scientists = ("agassiz", "agnesi", "alas", "alcala", "alexandria", "ali",
              "alvarez", "ampere", "anderson", "anning", "apgar", "arber",
              "arrhenius", "avery", "avogadro", "babbage", "bacon", "bain",
              "baird", "banks", "barba", "bardeen", "barkla", "battani",
              "battuta", "bayliss", "beadle", "beckman", "becquerel",
              "behring", "bell", "berliner", "bernard", "bernoulli",
              "berzelius", "bessemer", "bethe", "bhabha", "binet", "birdseye",
              "birkeland", "black", "blackwell", "blalock", "blodgett", "boas",
              "bohm", "bohr", "boltzmann", "born", "bosch", "bose", "bothe",
              "boyle", "bragg", "brahe", "brand", "brandt", "braun", "bretz",
              "broglie", "brongniart", "brown", "buck", "buckland", "buffon",
              "bunsen", "burbank", "burnell", "burnet", "cabrera", "cajal",
              "cantor", "carson", "carver", "cavendish", "celsius", "chadwick",
              "chandrasekhar", "chargaff", "chomsky", "chu", "clark", "cnidus",
              "cockcroft", "compton", "copernicus", "cori", "cousteau",
              "crick", "croll", "culpeper", "curie", "cuvier", "czerny",
              "daimler", "dalton", "dana", "darwin", "davy", "debye",
              "delbruck", "deluc", "descartes", "diesel", "dirac", "divis",
              "dobzhansky", "drake", "drexler", "dumont", "eccles",
              "eddington", "edison", "ehrlich", "einstein", "eklund", "elder", "elion",
              "erdosz", "euler", "farabi", "faraday", "fermat", "fermi",
              "feynman", "fischer", "fisher", "fleming", "florey", "ford",
              "forest", "foucault", "franklin", "freud", "friedman", "galilei",
              "galton", "galvani", "gamow", "gaposchkin", "gardner", "gauss",
              "germain", "gibbs", "gilbert", "glashow", "goddard", "gold",
              "goodall", "gould", "guericke", "haber", "haeckel", "hahn",
              "haller", "halley", "hardy", "harriot", "harvey", "hawking",
              "haxel", "heisenberg", "helmholtz", "helmont", "herbertsson", "herschel",
              "hertz", "herzfeld", "hevesy", "hewish", "hilbert", "hilleman",
              "hirase", "hodgkin", "hooke", "hopkins", "hopper", "hornby",
              "horner", "houssay", "hoyle", "hubble", "humboldt", "hurston",
              "hutton", "huygens", "illy", "ising", "ito", "jemison", "jenner",
              "jensen", "joule", "jr", "julian", "kaku", "kapitsa", "kekule",
              "kelsey", "kendrick", "kepler", "khalili", "khan", "khayyam",
              "khwarizmi", "kinsey", "kirchoff", "klaproth", "knutsson", "koch",
              "kraepelin", "kronecker", "kuhn", "kwolek", "lagrange",
              "lamarck", "lamarr", "land", "landsteiner", "laplace", "laue",
              "lavoisier", "lawrence", "leavitt", "lee", "leeuwenhoek",
              "lehmann", "leibniz", "lemaitre", "leoniceno", "leopold",
              "libby", "liebig", "linnaeus", "lister", "locke", "lorentz",
              "lorenz", "lovelace", "lowell", "lyell", "lysenko", "mach",
              "malpighi", "mann", "marcet", "marconi", "margulis", "matzinger",
              "maury", "maxwell", "mayer", "mayr", "mcclintock", "meitner",
              "mendel", "mendeleev", "mesmer", "meucci", "michell",
              "michelson", "milankovic", "milgram", "mitchell", "molina",
              "montalcini", "morgan", "morse", "moseley", "nakaya", "napier",
              "natta", "needham", "neumann", "newton", "nicolle",
              "nightingale", "noakes", "nobel", "noether", "nye", "oersted",
              "ohm", "onnes", "oppenheimer", "origin", "ostwald", "oughtred",
              "particle", "pascal", "pasteur", "pauli", "pauling", "pausch",
              "pavlov", "penfield", "perelman", "perey", "perkin",
              "philoponus", "philosophy", "piaget", "pinel", "pisa", "planck",
              "poincare", "popper", "potter", "priestley", "ptolemy",
              "quetelet", "quimby", "qurra", "raman", "ramanujan", "ramsay",
              "ray", "rays", "redi", "revenge", "ride", "riemann", "rontgen",
              "rorschach", "ross", "rushd", "rutherford", "sagan", "salam",
              "salk", "sanger", "schottky", "schrodinger", "schwann",
              "seaborg", "selye", "sherrington", "shoemaker", "siemens",
              "simpson", "skinner", "smith", "soddy", "somerville",
              "sommerfeld", "staudinger", "steno", "stevens", "strauss",
              "swainson", "system", "szilard", "tartaglia", "teller", "tesla",
              "thompson", "thomson", "thoreau", "thorne", "tombaugh",
              "tonegawa", "torricelli", "townes", "tu", "turing", "universe",
              "urey", "venter", "vernadsky", "vesalius", "vinci", "virchow",
              "virtanen", "volhard", "volta", "waksman", "wald", "wallace",
              "wallis", "walton", "watson", "watt", "wegener", "wheeler",
              "wiles", "wilkins", "willis", "wilson", "wingqvist",
              "winogradsky", "woese", "wohler", "wright", "wrong", "wundt",
              "yang", "zewail", )

animals = ("aardvark", "armadillo", "axolotl", "babirusa", "badger",
           "bandicoot", "bilby", "blobfish", "booby", "capybara", "cassowary",
           "cockatoo", "cockchafer", "colugo", "coot", "dugong", "echidna",
           "emu", "fennec", "frog", "frogmouth", "gaur", "gerenuk", "gharial",
           "hagfish", "hellbender", "hyrax", "jerboa", "koala", "lamprey",
           "lemming", "loon", "lumpsucker", "lyrebird", "manatee", "mandril",
           "mara", "moose", "muntjac", "narwhal", "numbat", "okapi", "olm",
           "pangolin", "parrotfish", "peccary", "platypus", "potoroo",
           "quagga", "quoll", "seadragon", "shoebill", "shrew", "sloth",
           "sparklemuffin", "sunfish", "tapir", "tardigrade", "tenrec", "tit", "titmouse",
           "umbrellabird", "vole", "wobbegong", "wolverine", "wombat", "yak",
           "zebu", )

nouns = (*scientists, *animals)

def memoname(allow_hyphens = True, category = 'all'):
    if category == 'all':
        things = nouns
    elif category == 'scientists':
        things = scientists
    elif category == 'animals':
        things = animals
    else:
        raise ValueError(f"There's no fucking category called '{category}'!")
    if allow_hyphens:
        a = adjectives
        n = things
    else:
        a = tuple(filter(lambda s : '-' not in s, adjectives))
        n = tuple(filter(lambda s : '-' not in s, things))
    return f"{random.choice(a)}_{random.choice(n)}"
