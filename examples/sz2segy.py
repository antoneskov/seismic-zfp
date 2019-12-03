import sys
from seismic_zfp.conversion import SzConverter


def main():
    if len(sys.argv) != 3:
        raise RuntimeError("This example accepts exactly 2 arguments: input_file & output_file")

    SzConverter(sys.argv[1]).convert_to_segy(sys.argv[2])


if __name__ == '__main__':
    main()
