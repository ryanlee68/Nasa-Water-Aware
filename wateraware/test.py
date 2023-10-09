# POLYGON((-66.8372838 17.8811922,-66.8372838 18.4947813,-65.6695563 18.4947813,-65.6695563 17.8811922,-66.8372838 17.8811922))
strr = "POLYGON((-66.8372838 17.8811922,-66.8372838 18.4947813,-65.6695563 18.4947813,-65.6695563 17.8811922,-66.8372838 17.8811922))"

# lst = poly[9:-2].replace(",", " ").split()
# result = []
# dictlist = []
# for i in range(0, len(lst), 2):
#     if i + 1 < len(lst):
#         result.append(lst[i + 1])
#         result.append(lst[i])
#     else:
#         # If there's only one element left, append it as is
#         result.append(lst[i])
# # print(result)

# for i in range(len(result)-2):
#     dictlist.append({"lat": result[i], "lng": result[i+1]})
    

# print(dictlist)

main_polys = []
pp = []
poly = {}

lst = strr[9:-2].replace(",", " ").split()
result = []
for j in range(0, len(lst), 2):
    if j + 1 < len(lst):
        result.append(lst[j + 1])
        result.append(lst[j])
    else:
        # If there's only one element left, append it as is
        result.append(lst[j])

print(result)


out = []
for i in range(0, len(result), 2):
    lat = float(result[i])  # Convert to float
    lng = float(result[i + 1])  # Convert to float
    # Create a dictionary with "lat" and "lng" keys and their respective values
    location_dict = {"lat": lat, "lng": lng}
    # Append the dictionary to the result list
    out.append(location_dict)

print(out)