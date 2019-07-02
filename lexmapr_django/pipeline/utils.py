from argparse import Namespace
from os.path import abspath
from tempfile import TemporaryDirectory

from lexmapr.pipeline import run


def run_lexmapr(input_file, config_file, full_format):
    """Run LexMapr package with specified arguments."""

    # Need to convert InMemoryUploadedFile values to actual files
    with TemporaryDirectory() as tmp_dir:
        tmp_input_path = abspath(tmp_dir + "/input.csv")
        tmp_output_path = abspath(tmp_dir + "/output.tsv")

        with open(tmp_input_path, "ab") as tmp_input_fp:
            for input_file_chunk in input_file.chunks():
                tmp_input_fp.write(input_file_chunk)

        run(Namespace(input_file=tmp_input_path, config=None,
                      format=full_format, output=tmp_output_path,
                      version=False, bucket=False))

        with open(tmp_output_path, "r") as tmp_output_fp:
            ret = tmp_output_fp.read()

    return ret
