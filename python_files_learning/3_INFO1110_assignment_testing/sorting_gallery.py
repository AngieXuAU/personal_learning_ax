'''
Angelina Xu
560686845
wexu0193
'''



def skip_this_image(file_object):

    new_line = file_object.readline()
    
    while "Title: " not in new_line and new_line != "":     # prevent an infinite string at the end
        # print(f"skipped {new_line.strip("\n")}")
        new_line = file_object.readline()

    return new_line


def view_gallery():
    gallery = {}

    try:
        # gather the list of pictures
        with open("gallery.txt", "r") as pictures_unsorted:     # opens the file


            line = pictures_unsorted.readline()

            while line != "":                                               # looping through the file using while because it is more elegant with the skip_this_image function

                if "Title: " in line:                                       # collate the titles
                    temp_title = line.strip()         

                    # print(f"checking what to do with {temp_title}")

                    if temp_title in gallery:                   
                        # print(f"about to skip this iteration of {temp_title}")

                        line = skip_this_image(pictures_unsorted)      # skip it if the title is already in the gallery
                        
                        continue
                        # print(pictures_unsorted.readline())
                        # exit()
                    else:
                        # print(f"adding {temp_title} to the collection!")
                        gallery[temp_title] = ""                # if not, add it to the dictionary as an empty string

                else:
                    gallery[temp_title] += line                 # add all the subsequent lines which do not have "title"
                
                line = pictures_unsorted.readline()             # start the loop again00

            collection = sorted(gallery.items())                # creates a dictionary "collection"

            for item, pic in collection:
                print(item)

                print(pic.strip("\n"))


    except FileNotFoundError:
        print("No images found in database.")
        return None


view_gallery()