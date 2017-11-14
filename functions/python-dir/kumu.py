import sys
import speech_recognition as sr
# use gRPCs if the files get complex and microservices are a must
def add(data):
    if data == "Rohan":
        data = "Hi Rohan, Fuck You!"
    print(data)

if __name__ == '__main__':
    data = sys.argv[1]
    add(data)
