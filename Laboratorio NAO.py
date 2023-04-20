import sys
from naoqi import ALProxy

def main(robotIP):

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 53119)
        tts = ALProxy("ALTextToSpeech", "127.0.0.1", 53119)
        part = 'Arms'
        body_names = motion_proxy.getBodyNames(part)
        speed = float(0.1) 

        posturasProxy.goToPosture("StandInit", 2.0)
        
        motion_proxy.moveInit()
        motion_proxy.setAngles('LShoulderPitch',  -0.6, speed)
        motion_proxy.setAngles('RShoulderPitch',  -0.6, speed)
        time.sleep(2)
        postureProxy.goToPosture("Sit", 2.0)
        postureProxy.goToPosture("StandInit", 2.0)
        tts.say("Termine")
        

    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    

   
    


if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python alrobotposture.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
