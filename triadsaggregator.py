import pandas as pd
import argparse
import json


def append_to_file(name, dict):
    json.dump(dict, open(name, "w"))


def read_content_from_file(name):
    try:
        return json.load(open(name))
    except:
        return {}


def generate_qw_agg(df, input_file):
    print("# of Triads vs query window", len(df.index))
    file_name = input_file.split(".")[0]
    datekey = file_name.split("-")[1]
    tod = file_name.split("-")[2]
    qw = file_name.split("-")[3]
    wh = file_name.split("-")[4]

    dict1_file_name = "qw_analysis_" + wh
    dict2_file_name = "tod_analysis_"+wh

    content_as_dict = read_content_from_file(dict1_file_name)
    inner_dict ={}
    orig_val = 0
    if content_as_dict:
        if datekey in content_as_dict:
            inner_dict = content_as_dict[datekey]
            if qw in inner_dict:
                orig_val = inner_dict[qw]
            value = orig_val + len(df.index)
            inner_dict[qw] = value
        content_as_dict[datekey] = inner_dict
    else:
        inner_dict[qw] = len(df.index)
        content_as_dict[datekey]= inner_dict

    append_to_file(dict1_file_name, content_as_dict)

    content_as_dict = read_content_from_file(dict2_file_name)
    inner_dict ={}
    orig_val = 0
    if content_as_dict:
        if datekey in content_as_dict:
            inner_dict = content_as_dict[datekey]
            if tod in inner_dict:
                orig_val = inner_dict[tod]
            value = orig_val + len(df.index)
            inner_dict[tod] = value
        content_as_dict[datekey] = inner_dict
    else:
        inner_dict[tod] = len(df.index)
        content_as_dict[datekey]= inner_dict

    append_to_file(dict2_file_name, content_as_dict)


def traid_aggregator(input_file):
    df = pd.read_csv(input_file, delimiter=",", header=None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)
    generate_qw_agg(df,input_file)


def main():
    message = ("Aggregator for Triads output file exploration - Creates aggregated json o/p using the triads O/P file ")
    parser = argparse.ArgumentParser(message,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--triad_file", type=str, required=False,
                        help="The triad file(s) to use.",
                        default="triads-0204-2015-15-nonwh.csv")
    FLAGS = parser.parse_args()
    traid_aggregator(FLAGS.triad_file)


if __name__ == '__main__':
    main()
