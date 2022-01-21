import argparse


def arg_helper() -> []:
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-m", "--model", default=None, help="path to Model File ")
    arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
    arg_parse.add_argument("-d", "--directory", default=None, help="path to Directory with Images")
    args = vars(arg_parse.parse_args())
    return args
