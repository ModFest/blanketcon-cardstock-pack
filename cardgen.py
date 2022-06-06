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
    "additional_banners": ("Additional Banners", "Darkhax", "campgrounds", "decoration", "???"),
    "allium": ("Allium", "hugeblank, Patbox, BasiqueEvangelist", "deepwoods", "tech", "Arathain"),
    "arcanus_2": ("Arcanus 2", "Cammie, Will BL, MrSterner, ArathainFarqoe", "campgrounds", "magic", "Arathain"),
    "architecture_extensions": ("Architecture Extensions", "WoodierTexas", "starfall", "decoration", "???"),
    "archon": ("Archon", "Safro", "campgrounds", "magic", "Arathain"),
    "armor_stand_editor": ("Armor Stand Editor", "Patbox", "midway", "tech", "Arathain"),
    "aura": ("Aura", "maximum, DrRubisco", "lakeside", "magic", "Arathain"),
    "aurora_decor": ("Aurora's Decorations", "LambdAurora", "starfall", "decoration", "Arathain"),
    "automobility": ("Automobility", "FoundationGames", "springtide", "mech", "Arathain"),
    "bagels_baking": ("Bagel's Baking", "hugeblank, Aye, Solcat, Koritsi, ChocolateFrog18", "deepwoods", "nature", "Arathain"),
    "bewitchment": ("Bewitchment", "Bewitchment Team", "todo", "magic", "Arathain"),
    "bewitchment_plus": ("Bewitchment Plus", "MrSterner", "todo", "magic", "Arathain"),
    "bing_bing_wahoo": ("Bing Bing Wahoo", "Tropheus Jay, Soggy Cereal", "deepwoods", "mech", "Arathain"),
    "bits_and_chisels": ("Bits and Chisels", "ThatTrollzer", "starfall", "decoration", "Arathain"),
    "botania": ("Botania", "Vazkii, Williewillus, Hubry, Alwinfy", "industries", "tech", "Arathain"),
    "build_battle": ("Build Battle", "NucleoidMC", "deepwoods", "tech", "Arathain"),
    "campanion": ("Campanion", "Terraformers", "campgrounds", "nature", "???"),
    "cardstock": ("CardStock", "Repulica, LemmaEOF", "campgrounds", "tech", "Arathain"),
    "cc_prometheus": ("ComputerCraft: Prometheus", "SquidDev", "overlook", "tech", "Arathain"),
    "cc_restitched": ("ComputerCraft: Restitched", "Merith, Patbox, SquidDev", "overlook", "tech", "Arathain"),
    "chocolate_bar": ("Chocolate Bar", "woodiertexas", "industries", "creature", "Arathain"),
    "chromatic_currents": ("Chromatic Currents", "Fusion Flux", "starfall", "mech", "Arathain"),
    "consistency_plus": ("Consistency Plus", "Cart3r, Tropheus Jay, Siuol", "deepwoods", "decoration", "Arathain"),
    "create": ("Create", "Create Fabric Team", "deepwoods", "mech", "Arathain"),
    "culinaire": ("Culinaire", "Dawn Team", "industries", "creature", "Arathain"),
    "dark_paintings": ("Dark Paintings", "Darkhax", "campgrounds", "decoration", "Darkhax"),
    "dark_utilities": ("Dark Utilities", "Darkhax", "campgrounds", "mech", "Darkhax"),
    "decorative": ("Decorative", "Motschen", "lakeside", "decoration", "Arathain"),
    "destroy_the_monument": ("Destroy The Monument", "NucleoidMC", "midway", "creature", "Arathain"),
    "double_jump_attribute": ("Double Jump Attribute", "Amy", "deepwoods", "mech", "Arathain"),
    "dyeable_fishing_lines": ("Dyeable Fishing Lines", "Fusion Flux", "deepwoods", "decoration", "Arathain"),
    "ears": ("Ears", "unascribed", "campgrounds", "decoration", "Arathain"),
    "ecotones": ("Ecotones", "supercoder79", "starfall", "nature", "Arathain"),
    "emi": ("EMI", "Emi", "campgrounds", "tech", "Arathain"),
    "enchancement": ("Enchancement", "MoriyaShiine", "starfall", "magic", "Arathain"),
    "endermantic_overhaul": ("Endermantic Overhaul", "anonym123", "campgrounds", "mech", "Arathain"),
    "extended_drawers": ("Extended Drawers", "MattiDragon", "lakeside", "mech", "Arathain"),
    "fabulously_optimized": ("Fabulously Optimized", "robotkoer", "starfall", "tech", "Arathain"),
    "flamingo": ("Flamingo", "copygirl, Vexatos", "campgrounds", "tater", "Arathain"),
    "flowery_structures": ("Flowery Structures", "JustAnUmbreon", "deepwoods", "nature", "Arathain"),
    "flying_fluxery": ("Flying Fluxery", "Fusion Flux", "todo", "mech", "Arathain"),
    "fortress": ("Fortress", "NucleoidMC", "midway", "tech", "Arathain"),
    "fusions_grapples": ("Fusion's Grapples", "Fusion Flux", "springtide", "mech", "Arathain"),
    "goml_reserved": ("Get Off My Lawn ReServed", "Patbox, Draylar", "midway", "tech", "Arathain"),
    "guard_villagers": ("Guard Villagers", "MrSterner", "todo", "mech", "Arathain"),
    "haema": ("Haema", "Will BL", "campgrounds", "magic", "Arathain"),
    "half_doors": ("Half Doors", "Amy", "deepwoods", "decoration", "Arathain"),
    "hex_casting": ("Hex Casting", "Petrak@, Alwinfy, Wiresegal", "starfall", "magic", "Arathain"),
    "hip_hoppers": ("Hip Hoppers", "Fusion Flux", "springtide", "mech", "Arathain"),
    "hud_overhaul": ("HUD Overhaul", "XanderStuff", "todo", "tech", "Arathain"),
    "icy_incitement": ("Icy Incitement", "Amy", "deepwoods", "mech", "Arathain"),
    "incorporeal": ("Incorporeal 3", "quat, Artemis System", "industries", "tech", "Arathain"),
    "inspecio": ("Inspecio", "LambdAurora, Emi", "todo", "tech", "Arathain"),
    "iris": ("Iris", "IMS", "todo", "tech", "Arathain"),
    "jamtastic": ("Jamtastic", "jamalam", "springtide", "creature", "Arathain"),
    "kiln": ("Kiln", "LemmaEOF, ZestyBlaze, BluKat", "campgrounds", "mech", "Arathain"),
    "lovely_snails": ("Lovely Snails", "LambdAurora", "starfall", "creature", "Arathain"),
    "matchbox": ("Matchbox", "Sunroses", "campgrounds", "mech", "Arathain"),
    "mbembe": ("Mbembe", "ArathainFarqoe, Mango, Coolrex, Ninni, Zae", "springtide", "creature", "Arathain"),
    "milk_plus": ("Milk+", "Tropheus Jay", "springtide", "nature", "Arathain"),
    "now_playing": ("Now Playing", "AppleTheGolden", "deepwoods", "tech", "Arathain"),
    "overweight_farming": ("Overweight Farming", "MrSterner", "todo", "nature", "Arathain"),
    "oxidized": ("Oxidized", "Safro", "springtide", "decoration", "Arathain"),
    "packages": ("Packages", "quat", "industries", "mech", "Arathain"),
    "pehkui": ("Pehkui", "Virtuoel", "starfall", "tech", "Arathain"),
    "pettable_bees": ("Pettable Bees", "Fusion Flux", "springtide", "nature", "Arathain"),
    "phonos": ("Phonos", "FoundationGames", "overlook", "mech", "Arathain"),
    "pigpen": ("Pig Pen Cipher", "Darkhax", "campgrounds", "tech", "Darkhax"),
    "player_pronouns": ("Player Pronouns", "Ash", "todo", "tech", "Arathain"),
    "polaroid_camera": ("Polaroid Camera", "Pigeon", "springtide", "mech", "Arathain"),
    "polymc": ("PolyMc", "TheEpicBlock", "midway", "tech", "Arathain"),
    "portal_cubed": ("Portal Cubed", "Portal Cubed team", "campgrounds", "tech", "Arathain"),
    "promenade": ("Promenade", "Dawn Team", "starfall", "nature", "Arathain"),
    "pswg": ("Galaxies: Parzi's Star Wars Mod", "PSWG Team", "springtide", "tech", "Arathain"),
    "purpeille": ("Purpeille", "acikek, VirtuaLilith, Trudle, Jeb_Kerm", "springtide", "magic", "VirtuaLilith"),
    "qcraft": ("qCraft: Reimagined", "acikek, VirtuaLilith", "todo", "mech", "Arathain"),
    "quakecraft": ("QuakeCraft", "NucleoidMC", "midway", "creature", "Arathain"),
    "quark": ("Quark", "wiresegal, Vazkii", "todo", "tech", "Arathain"),
    "reaping": ("Reaping Mod", "Jamalam", "overlook", "creature", "Arathain"),
    "recordable": ("Recordable", "burger", "lakeside", "mech", "Arathain"),
    "resounding": ("Resounding", "DrRubisco, iceGiant", "todo", "tech", "Arathain"),
    "riptide_rush": ("Riptide Rush", "Amy", "deepwoods", "tech", "Arathain"),
    "runelic": ("Runelic", "Darkhax", "campgrounds", "tech", "Darkhax"),
    "sandwichable": ("Sandwichable", "FoundationGames", "deepwoods", "nature", "Arathain"),
    "simple_crates": ("Simple Crates", "Sunroses", "campgrounds", "mech", "Arathain"),
    "simplevillagers": ("Simple Villagers", "samo_lego", "springtide", "mech", "Arathain"),
    "skywars": ("Skywars", "NucleoidMC", "midway", "tech", "Arathain"),
    "soul_ice": ("Soul Ice", "Siuol", "lakeside", "decoration", "Arathain"),
    "spacefactory": ("SpaceFactory", "reoseah", "overlook", "tech", "Arathain"),
    "tatercart": ("TaterCart", "Patbox", "midway", "mech", "???"),
    "taterzens": ("Taterzens", "samo_lego", "todo", "tech", "Arathain"),
    "terracraft": ("TerraCraft", "SimplyCmd, RiverOaken", "campgrounds", "nature", "Arathain"),
    "terrariamod": ("TerrariaMod", "Ryorama, Realz, Kelvin, Cepheus", "springtide", "nature", "Arathain"),
    "this_rocks": ("This Rocks!", "Motschen", "lakeside", "decoration", "Arathain"),
    "visible_barriers": ("Visible Barriers", "Amy", "deepwoods", "tech", "Arathain"),
    "xp_share": ("XP Share", "Sunroses", "todo", "tech", "Arathain"),
    "yungs_better_dtemples": ("YUNG's Better Desert Temples", "YUNGNICKYOUNG", "todo", "mech", "Arathain")
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
    kdl.write('\trarity ' + ('4' if rhf else '2') + '\n')
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
