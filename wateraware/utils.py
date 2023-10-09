
from wateraware import app
from .models import Enda

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


    return polys

def get_polys(county):
    main_polys = []
    meta = []
    with app.app_context():
        peter = Enda.query.filter_by(county=county, status="Endangered").all()
        temp_name = []
        for i in peter:
            pp = []
            poly = {}
            
            lst = i.poly_env[9:-2].replace(",", " ").split()
            for j in range(0, len(lst), 2):
                lat = float(lst[j+1])  # Convert to float
                lng = float(lst[j])
                location_dict = {"lat": lat, "lng": lng}
                pp.append(location_dict)
            main_polys.append(pp)
        
            out = {}
            if i.c_name not in temp_name:
                temp_name.append(i.c_name)
                out["name"] = i.c_name
                out["sci_name"] = i.sci_name
                out["desc"] = i.description
                out["img_url"] = i.img_url_2
                out["img_source"] = i.img_source
                meta.append(out)

    # unique_child_arrays = set()

    # # Create a new list to store the filtered mother array
    # filtered_mother_array = []

    # # Iterate through the mother array
    # for child_array in main_polys:
    # # Convert the child array to a tuple of dictionaries
    #     child_tuple = tuple(child_array)

    # # Check if the child array is unique
    #     if child_tuple not in unique_child_arrays:
    #     # If it's unique, add it to the filtered mother array and the set
    #         filtered_mother_array.append(child_array)
    #         unique_child_arrays.add(child_tuple)
    
    # print(main_polys)

    return main_polys, meta
