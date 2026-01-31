full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if (strength + intelligence +  charisma) != 7:
        return "The character should start with 7 points"

    fulldot_st = full_dot
    fulldot_st *= strength

    fulldot_int = full_dot
    fulldot_int *= intelligence

    fulldot_cha = full_dot
    fulldot_cha *= charisma

    emptydots_st = empty_dot
    emptydots_st *= 10 - strength

    emptydots_int = empty_dot
    emptydots_int *= 10 - intelligence

    emptydots_cha = empty_dot
    emptydots_cha *= 10 - charisma

    character = character_name + "\nSTR " + fulldot_st + emptydots_st + "\nINT " + fulldot_int + emptydots_int +  "\nCHA " + fulldot_cha + emptydots_cha

    return character


create_character("Occidi", 2, 3, 2)
