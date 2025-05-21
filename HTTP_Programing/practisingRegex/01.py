import re
pattern="malware"
text='''
Malware (a portmanteau of malicious software)[1] is any software 
intentionally designed to cause disruption to a computer, server,
 client, or computer network, leak private information, gain 
 unauthorized access to information or systems, deprive access to
   information, or which unknowingly interferes with the user's
     computer security and privacy.[1][2][3][4][5] Researchers 
     tend to classify malware into one or more sub-types (i.e.
       computer viruses, worms, Trojan horses, logic bombs, 
       ransomware, spyware, adware, rogue software, wipers and 
       keyloggers).[1]

Malware poses serious problems to individuals and businesses 
on the Internet.[6][7] According to Symantec's 2018 Internet 
Security Threat Report (ISTR), malware variants number has 
increased to 669,947,865 in 2017, which is twice as many 
malware variants as in 2016.[8] Cybercrime, which includes 
malware attacks as well as other crimes committed by computer, 
was predicted to cost the world economy US$6 trillion in 2021, 
and is increasing at a rate of 15% per year.[9] Since 2021, 
malware has been designed to target computer systems that run 
critical infrastructure such as the electricity distribution 
network.[10]

The defense strategies against malware differ according to the type of malware but most can be thwarted by installing antivirus software, firewalls, applying regular patches, securing networks from intrusion, having regular backups and isolating infected systems. Malware can be designed to evade antivirus software detection algorithms.[8]

History
Main article: History of computer viruses
For a chronological guide, see Timeline of computer viruses and 
worms.
The notion of a self-reproducing computer program can be traced 
back to initial theories about the operation of complex automata.
[11] John von Neumann showed that in theory a program could 
reproduce itself. This constituted a plausibility result in 
computability theory. Fred Cohen experimented with computer 
viruses and confirmed Neumann's postulate and investigated 
other properties of malware such as detectability and 
self-obfuscation using rudimentary encryption. His 1987 
doctoral dissertation was on the subject of computer 
viruses.[12] The combination of cryptographic technology
 as part of the payload of the virus, exploiting it for 
 attack purposes was initialized and investigated from 
 the mid-1990s, and includes initial ransomware and evasion 
 ideas.[13]


Before Internet access became widespread, viruses spread on 
personal computers by infecting executable programs or boot 
sectors of floppy disks. By inserting a copy of itself into 
the machine code instructions in these programs or boot sectors, 
a virus causes itself to be run whenever the program is run or 
the disk is booted. Early computer viruses were written for the 
Apple II and Mac, but they became more widespread with the 
dominance of the IBM PC and MS-DOS. The first IBM PC virus in 
the wild was a boot sector virus dubbed (c)Brain, created in 
1986 by the Farooq Alvi brothers in Pakistan.[14] Malware 
distributors would trick the user into booting or running from 
an infected device or medium. For example, a virus could make 
an infected computer add autorunnable code to any USB stick 
plugged into it. Anyone who then attached the stick to another 
computer set to autorun from USB would in turn become infected, 
and also pass on the infection in the same way.[15]

'''
match=re.search(pattern,text)
print(match)
