import json

zone_colors = {
    "Campgrounds": "aqua",
    "Starfall Ruins": "gray",
    "Lakeside Resort": "light_purple",
    "Overlook Point": "yellow",
    "Jacaranda Area": "dark_purple",
    "CL Industries": "dark_aqua",
    "Extant Deepwoods": "green",
    "Midway Park": "gold",
    "TODO: LOCATE ME": "red"
}

booth_cards = {
    # "allium": ("Allium", "hugeblank, Patbox, BasiqueEvangelist", "None", "tech", "Arathain"),
    "aurora_decor": ("Aurora's Decorations", "LambdAurora", "Starfall Ruins", "decoration", "Arathain"),
    # "bewitchment_plus": (),
    "bing_bing_wahoo": ("Bing Bing Wahoo", "Tropheus Jay, Soggy Cereal", "Extant Deepwoods", "mech", "Arathain"),
    "bits_and_chisels": ("Bits and Chisels", "ThatTrollzer", "Starfall Ruins", "decoration", "Arathain"),
    "cardstock": ("CardStock", "Repulica, LemmaEOF", "Campgrounds", "tech", "Arathain"),
    "cc_restitched": ("ComputerCraft: Restitched", "Merith, Patbox, SquidDev", "Overlook Point", "tech", "Arathain"),
    "chocolate_bar": ("Chocolate Bar", "woodiertexas", "CL Industries", "creature", "Arathain"),
    "consistency_plus": ("Consistency Plus", "Cart3r, Tropheus Jay, Siuol", "Extant Deepwoods", "decoration", "Arathain"),
    "destroy_the_monument": ("Destroy The Monument", "NucleoidMC", "Midway Park", "creature", "Arathain"),
    "fabulously_optimized": ("Fabulously Optimized", "robotkoer", "Starfall Ruins", "tech", "Arathain"),
    # "guard_villagers": (),
    "haema": ("Haema", "Will BL", "Campgrounds", "magic", "Arathain"),
    # "iris": (),
    "jamtastic": ("Jamtastic", "jamalam", "Jacaranda Area", "creature", "Arathain"),
    "lovely_snails": ("Lovely Snails", "LambdAurora", "Starfall Ruins", "creature", "Arathain"),
    "mbembe": ("Mbembe", "ArathainFarqoe, Mango, Coolrex, Ninni, Zae", "Jacaranda Area", "creature", "Arathain"),
    "milk_plus": ("Milk+", "Tropheus Jay", "Jacaranda Area", "nature", "Arathain"),
    "now_playing": ("Now Playing", "AppleTheGolden", "Extant Deepwoods", "tech", "Arathain"),
    # "overweight_farming": (),
    "phonos": ("Phonos", "FoundationGames", "Overlook Point", "mech", "Arathain"),
    "polymc": ("PolyMc", "TheEpicBlock", "Midway Park", "tech", "Arathain"),
    "portal_cubed": ("Portal Cubed", "Portal Cubed team", "Campgrounds", "tech", "Arathain"),
    # "qcraft": (),
    "quakecraft": ("QuakeCraft", "NucleoidMC", "Midway Park", "creature", "Arathain"),
    "reaping": ("Reaping Mod", "Jamalam", "Overlook Point", "creature", "Arathain"),
    # "resounding": (),
    "sandwichable": ("Sandwichable", "FoundationGames", "Extant Deepwoods", "nature", "Arathain")
    # "witherite": ()
}

langs = {}

with open('src/main/resources/data/blanketcon/cardstock/sets/blanketcon.kdl', 'w') as kdl:
    kdl.write('emblem "blanketcon:textures/gui/blanketcon.png"\n')
    for key, info in booth_cards.items():
        name, authors, location, frame, artist = info

        # lang entry
        langs['card.blanketcon.blanketcon.' + key] = name
        langs['card.blanketcon.blanketcon.' + key + '_rhf'] = name

        # kdl entries
        kdl.write('card "' + key + '" {\n')
        kdl.write('\trarity 1\n')
        kdl.write('\tinfo text="Located in ' + location + '" color="' + zone_colors[location] + '"\n')
        kdl.write('\t lore {\n')
        kdl.write('\t\t- text="by ' + authors + '" color="gray"\n')
        kdl.write('\t}\n')
        kdl.write('\tartist "' + artist + '"\n')
        kdl.write('\tdate "2022"\n')
        kdl.write('}\n')
        kdl.write('card "' + key + '_rhf" {\n')
        kdl.write('\trarity 2\n')
        kdl.write('\tinfo text="Located in ' + location + '" color="' + zone_colors[location] + '"\n')
        kdl.write('\t lore {\n')
        kdl.write('\t\t- text="by ' + authors + '" color="gray"\n')
        kdl.write('\t}\n')
        kdl.write('\tartist "' + artist + '"\n')
        kdl.write('\tdate "2022"\n')
        kdl.write('}\n')

        # asset jsons
        with open('src/main/resources/assets/blanketcon/models/item/card/blanketcon/' + key + '.json', 'w') as model:
            mjson = {
                "parent": "cardstock:builtin/card",
                "textures": {
                    "art": "blanketcon:item/card/art/" + key,
                    "frame": "blanketcon:item/card/frame/" + frame
                }
            }
            model.write(json.dumps(mjson, indent=4))
        with open('src/main/resources/assets/blanketcon/models/item/card/blanketcon/' + key + '_rhf.json', 'w') as rhf_model:
            rhf_mjson = {
                "parent": "cardstock:builtin/card",
                "textures": {
                    "art": "blanketcon:item/card/art/" + key,
                    "frame": "blanketcon:item/card/frame/" + frame,
                    "holo_left": "blanketcon:item/card/frame/" + frame + "_rhf_left",
                    "holo_center": "blanketcon:item/card/frame/" + frame + "_rhf_center",
                    "holo_right": "blanketcon:item/card/frame/" + frame + "_rhf_right"
                }
            }
            rhf_model.write(json.dumps(rhf_mjson, indent=4))

with open('src/main/resources/assets/blanketcon/lang/en_us.json', 'w') as lang:
    lang.write(json.dumps(langs, indent=4))
