from getbits import get_bits

filename = "sample.txt"

with open('lifetimes.txt', 'w') as file:
    pass
print("Lifetimes file 'lifetimes.txt' created.")

with open(filename, 'r') as file:

    RE0_Detected = False
    RE1_Detected = False
    RE1_2_Detected = False
    current_state = "Detecting RE0"

    #1st element of list stores RE1_Time (Word 1)
    #2nd element of list stores RE1_Time (Word 2, Bits 0-4)
    #3rd element of list stores RE1_2_Time (Word 1)
    #4th element of list stores RE1_2_Time (Word 2, Bits
    DecayTimes = ["","","",""]

    for line in file:
        if get_bits(line, 2, 7) == "1": #Trigger Event Detected, this resets all variables
            current_state = "Detecting RE0"
            DecayTimes = ["","","",""]
        
        #worried about detecting RE1 before RE0, or too may lines below, but problem for later
        if current_state == "Detecting RE0":
            if get_bits(line, 2, 5) == "1": #RE0 Detected:
                current_state = "Detecting RE1"
        
        if current_state == "Detecting RE1":
            if get_bits(line, 4, 5) == "1": #RE1 Detected:
                current_state = "Detecting RE1_2"
                DecayTimes[0] = get_bits(line, get_Time=True)
                DecayTimes[1] = get_bits(line, 2, 0, 5)
                continue
         
        if current_state == "Detecting RE1_2":
            if get_bits(line, 4, 5) == "1": #RE1_2 Detected:
                current_state = "Decay Found"
                DecayTimes[2] = get_bits(line, get_Time=True)
                DecayTimes[3] = get_bits(line, 2, 0, 5)
                with open('lifetimes.txt', 'a') as file:
                    file.write(f"{DecayTimes[0]} {DecayTimes[1]} {DecayTimes[2]} {DecayTimes[3]}\n")
                
                #resets again to search for next decay
                current_state = "Detecting RE0"
                DecayTimes = ["","","",""]



        


