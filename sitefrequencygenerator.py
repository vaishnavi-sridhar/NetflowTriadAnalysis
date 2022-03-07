import json

import pandas as pd



def main():
    df = pd.read_csv("netflowdatafile.csv", delimiter=",")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    #print(df)
    sub_df = df.groupby(['srcaddr','dstaddr']).size().reset_index(name='count').sort_values(['srcaddr'], ascending=True).head(5)
    print(sub_df)
    content_as_dict = read_content_from_file("sitefrequency.json")
    for index, row in sub_df.iterrows():
        outer_key = row['srcaddr']
        dst_key = row['dstaddr']
        dst_value = row['count']
        inner_dict = {}
        orig_val = 0

        if content_as_dict: #If the json file has contents
            if outer_key in content_as_dict: #If the src ip is contained in json file as outer dict key
                inner_dict = content_as_dict[outer_key]
                if dst_key in inner_dict:
                    orig_val = inner_dict[dst_key]
                value = orig_val + dst_value
                inner_dict[dst_key] = value
            else:
                inner_dict[dst_key] = dst_value
            content_as_dict[outer_key] = inner_dict
        else:
            inner_dict[dst_key] = dst_value
            content_as_dict[outer_key] = inner_dict
        append_to_file("sitefrequency.json", content_as_dict)


def read_content_from_file(name):
    try:
        return json.load(open(name))
    except:
        return {}


def append_to_file(name, dict):
    data = json.dumps(dict)
    with open(name, "w") as file:
        file.write(data)



if __name__ == '__main__':
    main()