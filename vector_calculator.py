from icecream import ic
from sigfig import round_sf
from numpy import cos, sin, degrees, radians, sqrt, arctan, abs
import warnings
warnings.filterwarnings("ignore")

def count(number):
    number = str(number).lower()
    if '-' in number:
        number = number.replace("-", "")
    numb_list = list(number)

    if '.' in numb_list and 'e' not in numb_list:
        decimal_location = numb_list.index('.')
        numb_list[decimal_location] = '0'
        return with_decimals(numb_list, decimal_location)
    elif '.' not in numb_list:
        return without_decimals(numb_list)
    elif 'e' in numb_list:
        return numb_list.index('e')-1
    else:
        ic("Something broke")

def with_decimals(numb_list, decimal_location):
    for index, digit in enumerate(numb_list):
        first_non_zero_location = 0
        if digit != '0':
            first_non_zero_location = index
            break
    if first_non_zero_location < decimal_location:
        return len(numb_list)-first_non_zero_location-1

    if first_non_zero_location > decimal_location:
        return len(numb_list) - first_non_zero_location

def without_decimals(numb_list):
    for index, digit in enumerate(numb_list):
        first_non_zero_location = 0
        if digit != '0':
            first_non_zero_location = index
            break

    for index, digit in reversed(list(enumerate(numb_list))):
        last_non_zero_location = 0
        if digit != '0':
            last_non_zero_location = index
            break

    return last_non_zero_location - first_non_zero_location + 1

def add_subtract(number1, number2, operator):
    number1, number2 = str(number1).lower(), str(number2).lower()
    numb1, numb2 = number1, number2
    if "e" in number1:
        numb1, _ = number1.split("e")
    if "e" in number2:
        numb2, _ = number2.split("e")
    if ("." in number1) and ("." in number2):
        temp1, temp2 = numb1.split("."), numb2.split(".")
        dec1, dec2 = len(temp1[-1]), len(temp2[-1])
        min_dec = min(dec1, dec2)
    else:
        min_dec = 0
    evaluation = eval(number1+operator+number2)
    return "%.*f" % (min_dec, evaluation)

def convert_2_num(input_str):
    if '.' in input_str:
        return float(input_str)
    else:
        return int(input_str)

def safe_cos(angle):
    result = cos(angle)
    if abs(result) < 1e-10: return 0
    return result

def safe_sin(angle):
    result = sin(angle)
    if abs(result) < 1e-10: return 0
    return result

def main(inputs):
    mag1, angle1 = inputs[0], inputs[1]
    mag2, angle2 = inputs[2], inputs[3]
    mag1_sig, angle1_sig = count(mag1), count(angle1)
    mag2_sig, angle2_sig = count(mag2), count(angle2)

    sig1, sig2 = min(mag1_sig, angle1_sig), min(mag2_sig, angle2_sig)
    angle1, angle2 = radians(angle1), radians(angle2)

    x1 = round_sf(mag1 * safe_cos(angle1), sig1)
    y1 = round_sf(mag1 * safe_sin(angle1), sig1)
    x2 = round_sf(mag2 * safe_cos(angle2), sig2)
    y2 = round_sf(mag2 * safe_sin(angle2), sig2)

    if "0" == x1[-1]:
        print("The X1 value has a zero at the end, so the significant figures of the answer may be wrong.")
    if "0" == x2[-1]:
        print("The X2 value has a zero at the end, so the significant figures of the answer may be wrong.")
    if "0" == y1[-1]:
        print("The Y1 value has a zero at the end, so the significant figures of the answer may be wrong.")
    if "0" == y2[-1]:
        print("The Y2 value has a zero at the end, so the significant figures of the answer may be wrong.")
    

    x1 = convert_2_num(x1)
    x2 = convert_2_num(x2)
    y1 = convert_2_num(y1)
    y2 = convert_2_num(y2)

    x, y = convert_2_num(add_subtract(x1, x2, "+")), convert_2_num(add_subtract(y1, y2, "+"))
    x_temp, y_temp = str(x), str(y)

    if ("." in x_temp) and ("." in y_temp):
        temp1, temp2 = x_temp.split("."), y_temp.split(".")
        mag = round(sqrt(x**2 + y**2), min(len(temp1[-1]), len(temp2[-1])))
    else:
        mag = int(round(sqrt(x**2 + y**2), 0))

    x_sig, y_sig = count(x), count(y)
    angle = convert_2_num(round_sf(degrees(arctan(y/x)), min(x_sig, y_sig)))

    if "-" in str(x) and "-" not in str(y):
        angle += 180
    elif "-" in str(y) and "-" not in str(x):
        angle += 360
    elif "-" in str(x) and "-" in str(y):
        angle += 180

    # For testing add answers as second parameter
    # if answers[0] != x1: ic(f"Not equal. Input: '{answers[0]}' Answer: '{x1}'")
    # if answers[2] != x2: ic(f"Not equal. Input: '{answers[2]}' Answer: '{x2}'")
    # if answers[1] != y1: ic(f"Not equal. Input: '{answers[1]}' Answer: '{y1}'")
    # if answers[3] != y2: ic(f"Not equal. Input: '{answers[3]}' Answer: '{y2}'")
    # if answers[4] != x: ic(f"Not equal. Input: '{answers[4]}' Answer: '{x}'")
    # if answers[5] != y: ic(f"Not equal. Input: '{answers[5]}' Answer: '{y}'")
    # if answers[6] != mag: ic(f"Not equal. Input: '{answers[6]}' Answer: '{mag}'")
    # if answers[7] != angle: ic(f"Not equal. Input: '{answers[7]}' Answer: '{angle}'")

    print(f"x1: {mag1} * cos({inputs[1]}) = {x1}")
    print(f"x2: {mag2} * cos({inputs[3]}) = {x2}")
    print(f"y1: {mag1} * cos({inputs[1]}) = {y1}")
    print(f"y2: {mag2} * cos({inputs[3]}) {y2}")
    print(f"x: {x1} + {x2} = {x}")
    print(f"y: {y1} + {y2} = {y}")
    print(f"Magnitude: sqrt({x}**2 + {y}**2) = {mag}")
    print(f"Angle: arctan({y}/{x}) = {angle}")

#main([3.2, 130, 2.3, 40.0], [-2.1, 2.5, 1.8, 1.5, -0.3, 4.0, 4.0, 90])
#main([34.0, 45, 20.0, 123], [24, 24, -10.9, 16.8, 13, 41, 43, 72])
#main([125, 30.0, 20.0, 225], [108, 62.5, -14.1, -14.1, 94, 48.4, 106, 27])
#main([3.1, 60.0, 1.4, 290], [1.6, 2.7, 0.48, -1.3, 2.1, 1.4, 2.5, 34])
#main([8.2, 120, 3.2, 250], [-4.1, 7.1, -1.1, -3.0, -5.2, 4.1, 6.6, 142])
#main([3.0, 90.0, 1.2, 180.0], [0, 3.0, -1.2, 0, -1.2, 3.0, 3.2, 112])
#main([30.0, 120, 5.1, 315], [-15, 26, 3.6, -3.6, -11, 22, 25, 117])
#main([300.0, 0, 25, 315], [300.0, 0, 18, -18, 318, -18, 319, 356.8])

# mag1 = convert_2_num(input("What is the magnitude of vector 1?\n"))
# angle1 = convert_2_num(input("What is the angle of vector 1?\n"))
# mag2 = convert_2_num(input("What is the magnitude of vector 2?\n"))
# angle2 = convert_2_num(input("What is the angle of vector 2?\n"))

# main([mag1, angle1, mag2, angle2])
main([3.58, 184, 2.05, 276])