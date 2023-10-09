
from wateraware import app
from .models import Enda

# based on city input, find nearest county
# def get_county(city=None, radius=None):
#     with app.app_context():
#         peter = Enda.query.filter_by(county="Niagara").all()
#         for i in peter:
#             print(i.c_name)

# get_county()

def get_meta(county):
    polys = []
    with app.app_context():
        peter = Enda.query.filter_by(county=county, status="Endangered").distinct()
        temp_name = []
        for i in peter:
            out = {}
            if i.c_name not in temp_name:
                temp_name.append(i.c_name)
                out["name"] = i.c_name
                out["sci_name"] = i.sci_name
                out["desc"] = i.description
                out["img_url"] = i.img_url_2
                out["img_source"] = i.img_source
                polys.append(out)
    # print(polys)
    # key_to_check = "name"
    # value_to_remove = 

    # # Use a list comprehension to remove dictionaries with the specified key and value
    # filtered_list = [d for d in list_of_dicts if d.get(key_to_check) != value_to_remove]


    return polys

def get_polys(county):
    main_polys = []
    polys = []
    with app.app_context():
        peter = Enda.query.filter_by(county=county, status="Endangered").all()
        for i in peter:
            pp = []
            poly = {}
            # poly["name"] = i.c_name
            # poly["sci_name"] = i.sci_name
            # poly["desc"] = i.description
            
            lst = i.poly_env[9:-2].replace(",", " ").split()
            result = []
            for j in range(0, len(lst), 2):
                if j + 1 < len(lst):
                    result.append(lst[j + 1])
                    result.append(lst[j])
                else:
                    # If there's only one element left, append it as is
                    result.append(lst[j])

            # for k in range(len(result)-2):
            #     pp.append({"lat": float(result[k]), "lng": float(result[k+1])})
            # main_polys.append(pp)
            

            for k in range(0, len(result), 2):
                lat = float(result[k])  # Convert to float
                lng = float(result[k + 1])  # Convert to float
                # Create a dictionary with "lat" and "lng" keys and their respective values
                location_dict = {"lat": lat, "lng": lng}
                # Append the dictionary to the result list
                pp.append(location_dict)
            main_polys.append(pp)

            # poly["poly"] = dictlist
            # poly["poly"] = i.poly_env
            # poly["img_url"] = i.img_url_2
            # poly["img_source"] = i.img_source
            polys.append(poly)
    return polys, main_polys
