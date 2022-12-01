import datetime
import getopt
import os
import sys

from tools.LogUtil import my_logger


def read_fasta(filename, outfile_path):
    with open(outfile_path, 'w') as out:
        with open(filename, 'r') as f:
            temp = ""
            strs = ""
            names = ""
            for line in f:
                if line.startswith('>'):
                    strs = temp
                    if (len(strs) != 0):
                        out.writelines('>' + names + "\n")
                        for j in range(len(strs)):
                            if (strs[j] != 'A' and strs[j] != 'C' and strs[j] != 'G' and strs[j] != 'T'):
                                out.write('N')
                            else:
                                out.write(strs[j])
                        out.write('\n')
                    names = line[1:-1]
                    temp = ""
                    continue
                if line.startswith('\n'):
                    continue
                temp += line[:-1]
            strs = temp
            out.writelines('>' + names + "\n")
            for j in range(len(strs)):
                if (strs[j] != 'A' and strs[j] != 'C' and strs[j] != 'G' and strs[j] != 'T'):
                    out.write('N')
                else:
                    out.write(strs[j])
            out.write('\n')


def SeqNHandleProcess(input_file_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    current_time = datetime.datetime.now().strftime('%b%d_%H-%M-%S')
    output_file_name = current_time + "_result_SeqNHandle.txt"
    output_file_path = os.path.join(output_path, output_file_name)
    return_data = dict()
    try:
        read_fasta(input_file_path, output_file_path)
        return_data['status'] = "success"
        return_data['result_path'] = output_file_path

    except Exception as ee:
        my_logger.error(ee)
        return_data['status'] = "failed"
        return_data['result_path'] = output_file_path
    return return_data


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    infile_path = ""
    outfile_path = ""
    for op, value in opts:
        if op == "-i":
            infile_path = value
            print(infile_path)
        elif op == "-o":
            outfile_path = value
            print(outfile_path)

    infile_path = "path_to_dir/example.fasta"
    outfile_path = "path_to_output/ouput.fasta"
    read_fasta(infile_path, outfile_path)
