import pycountry
from redishandler import intersection_iso_input


def handler(iso, input_list):
    if len(iso) > 3 or len(iso) < 2 or input_list == []:
        return
    # ISO 3166-1 alpha-2 and ISO 3166-1 alpha-3 support, ISO 3166-1 numeric is rubbish
    if len(iso) == 3:
        country_details = pycountry.countries.get(alpha_3=iso)
    else:
        country_details = pycountry.countries.get(alpha_2=iso)

    if country_details:
        iso = country_details.alpha_3
    else:
        return

    iso = iso.upper()

    res=intersection_iso_input(iso, input_list)

    # if we really insisted on mantaining the order.. uncomment following line:
    # res = [ elem for elem in input_list if elem in res ]

    return (
        {
            "iso": iso.lower(),
            "match_count": len(res), 
            "matches": list(res)
        }
    )
