import pycountry
import country_list
import time

from redishandler import add_set_to_redis
# SUPPORTS ALMOST ALL LANGUAGES
def ini_load():
    start = time.time()
    for country in pycountry.countries:
        country_alpha2 = country.alpha_2
        iso_acronyms_set = set()

        for language in country_list.available_languages():
            names_in_lang = dict(country_list.countries_for_language(language))
            if (to_add := names_in_lang.get(country_alpha2)) != None:
                iso_acronyms_set.add(to_add)

        add_set_to_redis(country.alpha_3, iso_acronyms_set)

    print("DONE")
    print(">>> Loaded in: ", time.time()-start,"sec <<<")
