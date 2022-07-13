import pycountry
from redishandler import intersection_set_input
#zistit ako je to s unicode-om

def handler(iso, input_list):
    if len(iso)>3 or len(iso)<2 or input_list==[]:
        return
    # ISO 3166-1 alpha-2 and ISO 3166-1 alpha-3 support, ISO 3166-1 numeric is rubbish
    if len(iso) == 2:
        country_details = pycountry.countries.get(alpha_2=iso)
    else:
        country_details = pycountry.countries.get(alpha_3=iso)

    if country_details:
        iso = country_details.alpha_3
    else:
        return

    iso = iso.upper()

    print(res:=intersection_set_input(iso, input_list))


    return (
        {
            "iso": iso.lower(),
            "match_count": len(res), 
            "matches": list(res)
        }
    )
