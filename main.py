from getbits import get_bits, get_lifetime

filename = "sample.txt"

with open('lifetimes.txt', 'w') as file:
    print("Lifetimes file 'lifetimes.txt' created.")



with open(filename, 'r') as file:

    #1st element of list stores RE1_Time (Word 1)
    #2nd element of list stores RE1_Time (Word 2, Bits 0-4)
    #3rd element of list stores RE1_2_Time (Word 1)
    #4th element of list stores RE1_2_Time (Word 2, Bits
    #5th element of list stores muon lifetimes

    DecayTimes = ["","","","",""]

    lines = file.readlines() # list of all lines in file

    for i in range(len(lines)):

        if len(lines[i].split(" ")) != 16:
            continue # skips lines that are not data

        if get_bits(lines[i], 2, 7) == "1": # trigger event detected, resets all variables
            DecayTimes = ["","","","",""]
            # checks for coincidence
            if get_bits(lines[i], 2, 5) == "1" and get_bits(lines[i], 4, 5) == "1":

                DecayTimes[0] = get_bits(lines[i], get_Time=True)
                DecayTimes[1] = get_bits(lines[i], 2, 0, 5)

                # Detecting RE1_2
                for j in range(i+1, len(lines)):
                    if int(get_bits(lines[j], 1, length=8), 16) - int(DecayTimes[0], 16) > 5000: #if it's been more than 5ms since RE1, reset to look for next decay
                        break
                    # detects an electron from a muon decay, which means we can stop
                    # looking for RE1_2 and reset to look for next decay
                    if get_bits(lines[j], 4, 5) == "1" and get_bits(lines[j], 2, 5) == "0":
                        # found a decay
                        DecayTimes[2] = get_bits(lines[j], get_Time=True)
                        DecayTimes[3] = get_bits(lines[j], 4, 0, 5)
                        DecayTimes[4] = get_lifetime(DecayTimes[0], DecayTimes[1], DecayTimes[2], DecayTimes[3])

                        with open('lifetimes.txt', 'a') as lifetime_file:
                            if True:  # ensures we only measure muon decays instead of time between muons

                                print("new lifetime: " + str(DecayTimes[4]))
                                lifetime_file.write(
                                    f"{DecayTimes[0]} {DecayTimes[1]} {DecayTimes[2]} {DecayTimes[3]} {DecayTimes[4]}\n")
                                break

                    # resets again to search for next decay
                DecayTimes = ["", "", "", "", ""]
