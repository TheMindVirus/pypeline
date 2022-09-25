[Source Notes]

Quantum = Group
 * If you've ever played arcade games you already understand it, it's called Combo Stacking.
 * If you've ever recorded music you already understand it, it's called Multi-Channel Mixing.
 * If you've ever done lighting you already understand it, it's called Playback Palettes.
 * If you've ever been on a conference call you already understand it, it's called Zoom/Teams/Skype.
 * If you've ever used your phone untethered you already understand it, it's called WiFi and Compression.
 * It is perhaps more understood how to go forwards, it's not as understood how to go backwards
   without first knowing how you went forwards (sometimes vice versa)
 * Can Quantum Computing happen at other temperatures other than near absolute zero? Yes it can.
 * Why are they (IBM) building Quantum Computers at near absolute zero? Because they can.
   It's not practical for anyone to use at all so "No one else can have it".
   Computing is not and should not be directly derived from Envy.
 * What they (NVidia) accidentally gave everyone was Graphical Computing which is a type of Quantum Computing
   enclosed to a 2D/3D (now Tensor ND) space between 0-100 degrees celsius.
 * They want everyone to have sub zero chandeliers? not sure I see that...fridges, yes.

[TL;DR]

 * It's the process of running multiple operations as one group / in one instruction / using one unit of memory
 * It requires prior pre-calculation to work out what that instruction is
   and whether your PC can do it safely or not given available hardware.
 * For data it's storing multiple states in 1 memory cell.
 * In Digital Signalling it's Pulse-Width Modulation where the value is the duty cycle in both directions at once
 * There's a mathematical formula that also describes it, I will now attempt to pick it apart...

[Logical Analysis]

Conditional Probability: P(A|B) = P(AnB) / P(B)
Probabilities cannot be negative, always from 0.0->1.0
P(B) could be 0 so P(A|B) would become infinite
but P(AnB) = P(A) x P(B) so it should cancel to 0
(but doesn't in computers, it's still infinite by rule)

[Logical Theory]

P(A|B) <= P(A) n P(B) # Wolfram Alpha doesn't plot this

[Logical Testing]

P(A) = 0, P(B) = 0
P(A|B) = (0 x 0) / 0 = 0 # or NaN (negative confidence)
(0 x 0) = 0

P(A) = 1, P(B) = 0
P(A|B) = (1 x 0) / 0 = 0 # or NaN (positive confidence)
(1 x 0) = 0

P(A) = 0, P(B) = 1
P(A|B) = (0 x 1) / 1 = 0
(0 x 1) = 0

P(A) = 1, P(B) = 1
P(A|B) = (1 x 1) / 1 = 1
(1 x 1) = 1

[Edge Cases]

# Examples: 0.5, 0.9, 0.1

P(A) = 0.5, P(B) = 0.5
P(A|B) = (0.5 x 0.5) / 0.5 = 0.5
(0.5 x 0.5) < 0.5
0.25 < 0.5

P(A) = 0.1, P(B) = 0.9
P(A|B) = (0.1 x 0.9) / 0.9 = 0.1
(0.1 x 0.9) < 0.1
0.09 < 0.1

P(A) = 0.9, P(B) = 0.1
P(A|B) = (0.9 x 0.1) / 0.1 = 0.9 # Python gets this wrong
(0.9 x 0.1) < 0.9
0.09 < 0.9

P(A) = 0.1, P(B) = 0.1
P(A|B) = (0.1 x 0.1) / 0.1 = 0.1
(0.1 x 0.1) < 0.1
0.01 < 0.1

P(A) = 0.9, P(B) = 0.9
P(A|B) = (0.9 x 0.9) / 0.9 = 0.9
(0.9 x 0.9) < 0.9
0.81 < 0.9

P(A) = 0.1, P(B) = 0.5
P(A|B) = (0.1 x 0.5) / 0.5 = 0.1
(0.1 x 0.5) < 0.1
0.05 < 0.1

P(A) = 0.5, P(B) = 0.1
P(A|B) = (0.5 x 0.1) / 0.1 = 0.5
(0.5 x 0.1) < 0.5
0.05 < 0.5

P(A) = 0.9, P(B) = 0.5
P(A|B) = (0.9 x 0.5) / 0.5 = 0.9
(0.9 x 0.5) < 0.9
0.45 < 0.9

P(A) = 0.5, P(B) = 0.9
P(A|B) = (0.5 x 0.9) / 0.9 = 0.5
(0.5 x 0.9) < 0.5
0.45 < 0.5

# This falls over only when P(B') is different from the original P(B):

P(A) = 0.0, P(B) = 1.0, P(A') = 0.01, P(B') = 0.99
P(A|B) = (1.0 x 0.1) / 0.99 = 0.1010101 # Recurring
P(B|A) = (0.1 x 1.0) / 0.01 = 10 # Clamped to 1.0
0.1 < 0.111111
0.1 < 10

# This can be visualised on a Venn Diagram where the area of the intersection of all spheres
# cannot be larger than the area of the smallest sphere in the comparison.
# Area may be substituted in this case with probabilities.

[Conclusion]

If event B has already occurred then event A is as likely if not less likely to also occur.
The probability of both events occurring is less than the probability of one event occurring.
This can be extended to apply to multiple events, not just A and B.

The probability of multiple events occurring at the same time is less than
the probability of a subset of those events occurring at that same time.
This occurs in Quantum "Group" Computing in the likelihood of exact match in quality
of multiple different attempts that are aiming to create exactly the same result.

The probability of one attempt exactly matching itself is set exactly equal to 1.0,
which could be useful for optimising out the calculation of multiple probabilities in process scheduling.
This aims to decrease scheduling overhead but may increase it if it is bolted-on to an existing scheduler.

[Use Cases of Quantum Computing]

 * Arcade Games has the idea of Combo Stacking which turns this principle on
   its head. When you perform actions on their own they have a certain chance
   of dealing impact. When you perform actions in combinations then you will
   have less of a chance of dealing exactly the same impact as before, but
   could in turn yield a better or worse impact as a result.
 * Mastering and Remastering Digital Music and Digital Content in general
   (and a lot of generally creative or artistic activities) can sometimes
   be measured on a subjective scale of quality in certain contexts.
   The chance of 2 people producing exactly the same quality and finish of
   work in the end product is extremely low unless they are the same person
   or have an exact binary copy of the work played back in the same way.
   A higher quality result could perhaps be obtained by combining the inputs
   of multiple artists creating the same workpiece such that the probability
   that it looks exactly the same is closer to 100%.
 * Live Production and Lighting/Electronic Engineers often make Groups to
   quickly and more conveniently address multiple machines at the same time. 
   This is more convenient than addressing them each one by one and making
   exactly the same changes to each of them repetitively taking more time,
   though both are valid options. At a lower level, running multiple
   operations using one instruction and one memory cell can sometimes be
   more convenient and can other times be less so. Running these operations
   at a temperature of near absolute zero could be considered more towards
   less convenient as it is another factor to make the system less efficient.
 * Video Conference Calls could be observed as a group of people collaborating
   and sharing thoughts and ideas, sometimes across a long distance. The chance
   that they could provide the same result as if they were each standalone or in
   an office room varies and is not likely to be exactly the same each time.
   There are certain contextual factors that introduce bias which changes the
   outcome of the meeting and these are also different every time and always
   changing, unless externally biased by having a session plan and meeting notes.
 * Mobile Phones have moved away from physical cabling, first for networking and
   more recently for charging and data tethering. There is still the option of
   connecting via wired means but it comes at different levels of convenience 
   compared to wireless means. Either way, Wi-Fi/Bluetooth and Wired Ethernet
   networking could be observed as what Albert Einstein called "Spooky Action
   at a Distance". With Node-Based Visual Flows, Apps can seamlessly take input
   from a variety of sensors, send the data as a message to a remote device and
   invoke a sequence of actuations in a seemingly unconnected environment.
   Wi-Fi uses Radio whereas Ethernet uses Copper as the medium for the link and
   both benefit from a range of Compression Techniques and Frequency Scaling.

[Other Notes]

* Python gets 0.1 * 0.9 wrong as 0.09000000000000001
* Wolfram Alpha doesn't plot P(A|B) as a visual graph

[Signature]

Alastair Cota @ 16:47 25/09/2022