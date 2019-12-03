import sys
from seismic_zfp.conversion import SegyConverter


def main():
    if len(sys.argv) != 3:
        raise RuntimeError("This example accepts exactly 2 arguments: input_file & output_file")

    SegyConverter(sys.argv[1], sys.argv[2]).convert(bits_per_voxel=2, blockshape=(64, 64, 4), method="Stream")


if __name__ == '__main__':
    main()
