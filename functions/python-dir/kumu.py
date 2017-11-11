import sys
# use gRPCs if the files get complex and microservices are a must
def add(data):
    print(data)

if __name__ == '__main__':
    data = sys.argv[1]
    add(data)
