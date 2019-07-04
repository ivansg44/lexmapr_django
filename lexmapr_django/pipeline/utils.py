from argparse import Namespace
from os.path import abspath
from tempfile import TemporaryDirectory

from lexmapr.pipeline import run


def run_lexmapr(input_file, config_file, full_format):
    """Run LexMapr package with specified arguments."""

    # Need to convert InMemoryUploadedFile values to actual files
    with TemporaryDirectory() as tmp_dir:
        tmp_input_path = tmp_dir + "/" + str(input_file)
        tmp_config_path = tmp_dir + "/" + str(config_file)
        tmp_output_path = tmp_dir + "/output.tsv"

        with open(tmp_input_path, "ab") as tmp_input_fp:
            for input_file_chunk in input_file.chunks():
                tmp_input_fp.write(input_file_chunk)

        with open(tmp_config_path, "ab") as tmp_config_fp:
            for config_file_chunk in config_file.chunks():
                tmp_config_fp.write(config_file_chunk)

        if full_format:
            format_val = "full"
        else:
            format_val = "basic"

        try:
            run(Namespace(input_file=tmp_input_path, config=tmp_config_path,
                          format=format_val, output=tmp_output_path,
                          version=False, bucket=False))
        except Exception:
            return "Oops! Something went wrong"

        with open(tmp_output_path, "r") as tmp_output_fp:
            ret = tmp_output_fp.read()

    return ret
