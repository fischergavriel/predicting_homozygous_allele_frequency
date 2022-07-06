#############################################################
# FILE: allele_combinations.py
# WRITER: Gavriel Fischer
# DESCRIPTION: A simple script to calculate the
#    expected frequency of homozygous genotypes out of a given
#    pool of alleles. Random assortment of alleles is assumed.
# PURPOSE: The script was written for the purpose of the
#    third and final "bioinformatics" lab report and in
#    honor of me beginning "Intro to CS" next week.
#############################################################
def homozygosity_freq(allele_pool):
    list_of_genotypes = []
    matching_index = 0
    for i in allele_pool:
        for j in allele_pool[matching_index:23]:
            list_of_genotypes.append([i, j])
        matching_index += 1

    homozygous_genotypes = 0
    for x in list_of_genotypes:
        if x[0] == x[1]:
            homozygous_genotypes += 1
    freq = (100 * homozygous_genotypes) / len(list_of_genotypes)
    print(str(round(freq, 2)) + "%")
    return freq
