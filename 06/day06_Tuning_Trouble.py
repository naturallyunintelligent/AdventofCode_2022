#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line)
    return data

def find_markers(datastream, marker_length):
    markers_received = []
    for i, line in enumerate(datastream):
        marker_test = []
        read = 0
        for index, char in enumerate(line):
            marker_test.append(char)
            read += 1
            if read < marker_length:
                continue
            elif read > marker_length:
                marker_test = marker_test[1:]
            if len(set(marker_test)) < marker_length:
                continue
            else:
                assert len(marker_test) == marker_length
                markers_received.append(index + 1)
                break

    return markers_received

if __name__ == '__main__':

    datastream = load_data(input_text_file)
    marker_end = []
    length_of_packet_marker = 4
    length_of_message_marker = 14
    for line in datastream:
        packet_markers_received = find_markers(datastream, length_of_packet_marker)
        message_markers_received = find_markers(datastream, length_of_message_marker)

    print(f"markers received at the following character indexes: {packet_markers_received}")
    print(f"markers received at the following character indexes: {message_markers_received}")

    #store answer as a comment
    #packet @ 1275
    #message @ 3605