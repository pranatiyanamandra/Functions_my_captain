
def most_frequent(string):
    string=string.lower()
    string_freq={}
    for alphabet in string:
        if alphabet not in string_freq.keys():
            string_freq[alphabet]=0
        string_freq[alphabet]+=1
    for key,value in string_freq.items():
        print("{}={:02d}".format(key,value))

input_string=input("Please enter a string ")            
most_frequent(input_string)            
