##
def bmiCalculation(*indata):
    return round(indata[0] / pow(indata[1], 2), 2)


def tempConverter(**indata):
    outdata = dict()
    if indata['degreeType'] == 'F':
        outdata['temp'] = (indata['temp'] - 32) * 5 / 9
        outdata['degreeType'] = 'C'
    elif indata['degreeType'] == 'C':
        outdata['temp'] = indata['temp'] * 9 / 5 + 32
        outdata['degreeType'] = 'F'
    return outdata

##
bmis = list()
bmis.append(bmiCalculation(80,1.7))
bmis.append(bmiCalculation(80,1.5))

convertedTemps = list()
convertedTemps.append(tempConverter(degreeType='F', temp=32))
convertedTemps.append(tempConverter(degreeType='C', temp=0))
