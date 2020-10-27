import colorSensor
import time


Threshold = 1500

def PCRTest(values):
    result = []
    for value in values:
        for component in value:
            if component > Threshold:
                result.append("O")
            else:
                result.append("X")
    return result


def main(args):
    colorSesnor = colorSensor.colorSensorArray()
    if colorSesnor.isConnected():
        colorSesnor.enableSensor()
        colorSesnor.setSensorMode(auto=True)
        colorSesnor.setSensorIT(2)
        while True:
            print PCRTest(colorSesnor.readColors(color=["green"]))
            #print colorSesnor.readColors(color=["green"])
            time.sleep(0.5)
    return 0


###########################

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
