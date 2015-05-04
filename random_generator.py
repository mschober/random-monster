from read_tsv_file import parse_tsv
import sys


character_xp_encounter_level = parse_tsv('tsv/character_xp_encounter_level.tsv')
monster_count_scale_factor = parse_tsv('tsv/monster_count_scale_factor.tsv')
xp_cr_mapping = parse_tsv('tsv/xp_cr_mapping.tsv')

print monster_count_scale_factor
