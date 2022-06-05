import json

zone_colors = {
    "campgrounds": "aqua",
    "starfall": "dark_gray",
    "lakeside": "light_purple",
    "overlook": "yellow",
    "springtide": "dark_purple",
    "industries": "dark_aqua",
    "deepwoods": "green",
    "midway": "gold",
    "todo": "red"
}

booth_cards = {
    "allium": ("Allium", "hugeblank, Patbox, BasiqueEvangelist", "deepwoods", "tech", "Arathain"),
    "aurora_decor": ("Aurora's Decorations", "LambdAurora", "starfall", "decoration", "Arathain"),
    # "bewitchment_plus": (),
    "bing_bing_wahoo": ("Bing Bing Wahoo", "Tropheus Jay, Soggy Cereal", "deepwoods", "mech", "Arathain"),
    "bits_and_chisels": ("Bits and Chisels", "ThatTrollzer", "starfall", "decoration", "Arathain"),
    "cardstock": ("CardStock", "Repulica, LemmaEOF", "campgrounds", "tech", "Arathain"),
    "cc_restitched": ("ComputerCraft: Restitched", "Merith, Patbox, SquidDev", "overlook", "tech", "Arathain"),
    "chocolate_bar": ("Chocolate Bar", "woodiertexas", "industries", "creature", "Arathain"),
    "consistency_plus": ("Consistency Plus", "Cart3r, Tropheus Jay, Siuol", "deepwoods", "decoration", "Arathain"),
    "destroy_the_monument": ("Destroy The Monument", "NucleoidMC", "midway", "creature", "Arathain"),
    "fabulously_optimized": ("Fabulously Optimized", "robotkoer", "starfall", "tech", "Arathain"),
    # "guard_villagers": (),
    "haema": ("Haema", "Will BL", "campgrounds", "magic", "Arathain"),
    # "iris": (),
    "jamtastic": ("Jamtastic", "jamalam", "springtide", "creature", "Arathain"),
    "lovely_snails": ("Lovely Snails", "LambdAurora", "starfall", "creature", "Arathain"),
    "mbembe": ("Mbembe", "ArathainFarqoe, Mango, Coolrex, Ninni, Zae", "springtide", "creature", "Arathain"),
    "milk_plus": ("Milk+", "Tropheus Jay", "springtide", "nature", "Arathain"),
    "now_playing": ("Now Playing", "AppleTheGolden", "deepwoods", "tech", "Arathain"),
    # "overweight_farming": (),
    "phonos": ("Phonos", "FoundationGames", "overlook", "mech", "Arathain"),
    "polymc": ("PolyMc", "TheEpicBlock", "midway", "tech", "Arathain"),
    "portal_cubed": ("Portal Cubed", "Portal Cubed team", "campgrounds", "tech", "Arathain"),
    # "qcraft": (),
    "quakecraft": ("QuakeCraft", "NucleoidMC", "midway", "creature", "Arathain"),
    "reaping": ("Reaping Mod", "Jamalam", "overlook", "creature", "Arathain"),
    # "resounding": (),
    "sandwichable": ("Sandwichable", "FoundationGames", "deepwoods", "nature", "Arathain"),
    # "witherite": (),
    "purpeille": ("Purpeille", "acikek, VirtuaLilith, Trudle, Jeb_Kerm", "springtide", "magic", "VirtuaLilith")
}

langs = {
    "location.blanketcon.campgrounds": "The Campgrounds",
    "location.blanketcon.starfall": "Starfall Ruins",
    "location.blanketcon.lakeside": "Lakeside Resort",
    "location.blanketcon.overlook": "Overlook Point",
    "location.blanketcon.springtide": "Springtide Fields",
    "location.blanketcon.industries": "CL Industries",
    "location.blanketcon.deepwoods": "Extant Deepwoods",
    "location.blanketcon.midway": "Midway Park",
    "location.blanketcon.todo": "TODO: Locate Me",
    "text.blanketcon.located": "Located in",
    "text.blanketcon.by": "By"
}
generated_cards = 0


def write_booth_card(kdl, key, info, rhf):
    name, authors, location, frame, artist = info

    path = key + '_rhf' if rhf else key

    # lang entry
    langs['card.blanketcon.blanketcon.' + path] = name

    # kdl entry
    kdl.write('card "' + path + '" {\n')
    kdl.write('\trarity ' + ('2' if rhf else '1') + '\n')
    kdl.write('\tinfo {\n')
    kdl.write('\t\t- translate="text.blanketcon.located" color="gray"\n')
    kdl.write('\t\t- text=" " color="gray"\n')
    kdl.write('\t\t- translate="location.blanketcon.' + location + '" color="' + zone_colors[location] + '"\n')
    kdl.write('\t}\n')
    kdl.write('\t lore {\n')
    kdl.write('\t\t- {\n')
    kdl.write('\t\t\t- translate="text.blanketcon.by" color="gray" \n')
    kdl.write('\t\t\t- text=" " color="gray"\n')
    kdl.write('\t\t\t- text="' + authors + '" color="green"\n')
    kdl.write('\t\t}\n')
    kdl.write('\t}\n')
    kdl.write('\tartist "' + artist + '"\n')
    kdl.write('\tdate "2022"\n')
    kdl.write('}\n')

    # asset jsons
    with open('src/main/resources/assets/blanketcon/models/item/card/blanketcon/' + path + '.json', 'w') as model:
        mjson = {
            "parent": "cardstock:builtin/card",
            "textures": {
                "art": "blanketcon:item/card/art/" + key,
                "frame": "blanketcon:item/card/frame/" + frame
            }
        }
        if rhf:
            mjson["textures"]["holo_left"] = "blanketcon:item/card/frame/" + frame + "_rhf_left"
            mjson["textures"]["holo_center"] = "blanketcon:item/card/frame/" + frame + "_rhf_center"
            mjson["textures"]["holo_right"] = "blanketcon:item/card/frame/" + frame + "_rhf_right"
        model.write(json.dumps(mjson, indent=4))
    print("Generated card " + path)


with open('src/main/resources/data/blanketcon/cardstock/sets/blanketcon.kdl', 'w') as kdl:
    kdl.write('emblem "blanketcon:textures/gui/blanketcon.png"\n')
    for key, info in booth_cards.items():
        write_booth_card(kdl, key, info, False)
        write_booth_card(kdl, key, info, True)
        generated_cards += 2
    print("Generated " + str(generated_cards) + " cards")

with open('src/main/resources/assets/blanketcon/lang/en_us.json', 'w') as lang:
    lang.write(json.dumps(langs, indent=4))
