'''Using os module'''

import os

def main():
    
    try:
        
        # grab filepath and filename, and print them out
        filename = os.path.abspath(os.path.join("data", "Consumer_Complaints.csv"))
        print(filename, '\n')

        # create file input stream
        fin = open(filename, 'r')

        # strip() removes the \n
        header = fin.readline().strip().split(',')
        print(header)

        # cycle through each line and append to list
        my_text = []
        for line in fin:
            my_text.append(line)

        print(my_text[:5])

    except:
        main()

if __name__ == "__main__":
    main()
