## Main function
def hello():
    import google_vision_tag_getter as gvt
    import wikipedia_and_summarize as wiki 
    import test_wiki as info
    import os

    #os.system("cd C:\\Users\\Jeswin\\flasksite")
    #os.system("set GOOGLE_APPLICATION_CREDENTIALS=C:\\Users\\Jeswin\\flasksite\\Hackhathon-65c2f11b3bbe.json")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Jeswin\\flasksite\\Hackhathon-65c2f11b3bbe.json"

    path="C:\\Users\\Jeswin\\flasksite\\opencv_frame_0.png"

    #master_list = []
    master_list = gvt.localize_objects(path)

    wiki_info = []
    '''
    for obj in master_list:
            wiki_info.append(wiki.wiki_ripoff(obj[0]))
    '''
    for obj in master_list:
            wiki_info.append(info.get_info(obj[0]))

    print(master_list)
    print(wiki_info)

    text_file = open("Output.txt", "w")

    text_file.write(wiki_info[0])

    text_file.close()
