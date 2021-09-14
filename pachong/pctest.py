from geopy.geocoders import Nominatim

loca = ["汉口站", "福星惠誉福星城", "金银湖"]
def   locas(loca):
    geolocator = Nominatim(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")  # 放ua
    location = geolocator.geocode(loca)  # 根据查相关信息
    # location = geolocator.reverse("52.509669, 13.376294")  #根据坐标查
    # print(location.address )
    print(loca + "," + str(location.latitude) + "," + str(location.longitude))
# print(location.longitude)
# print(location.altitude)
# print(location.point)
# print(location.raw)

if __name__ == '__main__':
    for x in loca:
        locas(str(x))
