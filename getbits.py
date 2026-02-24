#get_bits returns the bits of a specific word in a line of data
#   - line_text is the text of the line to analyze
#   - word_num is the number of the word in the line (beginning from 1, the time)
#   - bit_num is the number of the bit in the word (beginning from 0, rightmost bit btw)
#   - length is the number of bits to return (default is 1, will only use this for recording time 0-4 bits)
#   - get_Time is a boolean, whether you just want me to return the first word
def get_bits (line_text, word_num = 1, bit_num = 0, length = 1, get_Time = False):

    if(word_num < 1 or bit_num + length > 8):
        raise ValueError("Invalid word number or bit number/length combination.")
    
    words_list = line_text.split(" ")
    if get_Time:
        return words_list[0]
    
    value = int(words_list[word_num - 1], 16)
    binary_string = f'{value:08b}'
    reversedstring = binary_string[::-1]
    return reversedstring[bit_num: bit_num + length]

#get_lifetime takes in the times of RE1 and RE1_2 and calculates the lifetime of the muon in ns
def get_lifetime(RE1_Word_Time, RE1_Bit_Time, RE1_2_Word_Time, RE1_2_Bit_Time):
    #if(int(RE1_Bit_Time, 2) > 31 or int(RE1_2_Bit_Time, 2) > 31):
    #    print("Bit time greater than 31?")
    RE1_ns = (int(RE1_Word_Time, 16) * 40) + (int(RE1_Bit_Time, 2)/32 * 40)
    RE2_ns = (int(RE1_2_Word_Time, 16) * 40) + (int(RE1_2_Bit_Time, 2)/32 * 40)
    lifetime = RE2_ns - RE1_ns
    return lifetime
'''

#Tests
decay_lines = ["F309594F B3 00 33 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F3095950 00 00 00 28 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F3095950 00 30 00 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F309596A 00 00 2E 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F309596A 00 00 00 3D 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F3334EE8 AF 00 00 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F3334EE8 00 00 30 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F33D7599 00 00 00 2D 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000",
               "F338FF98 B3 00 33 00 00 00 00 00 00000002 000000.000 000000 V 00 8 +0000"]

print("\nTrigger Event Test: ")
for line in decay_lines:
    print(get_bits(line, 2, 7), end = ", ")
#Got: 1, 0, 0, 0, 0, 1, 0, 0, 1, 

print("\nValid Rising Edge 1 Test:")
for line in decay_lines:
    print(get_bits(line, 2, 5),end = ", ")
#Got: 1, 0, 0, 0, 0, 1, 0, 0, 1,

print("\nValid Rising Edge 2 Test:")
for line in decay_lines:
    print(get_bits(line, 4, 5),end = ", ")
#Got: 1, 0, 0, 1, 0, 0, 1, 0, 1,

#concern - erm for the lines where word 1 goes AF than 0, um i thought the time records were chronological??

print("\nTime Test (bits 0-4): ")
for line in decay_lines:
    print(int(get_bits(line, 2, 0, 5), 2),end = ", ")
#Got: 25, 0, 0, 0, 0, 30, 0, 0, 25,

print("\nTime Test (whole word): ")
for line in decay_lines:
    print(get_bits(line, get_Time=True),end = ", ")
#Got: F309594F, F3095950, F3095950, F309596A, F309596A, F3334EE8, F3334EE8, F33D7599, F338FF98,

'''
    

