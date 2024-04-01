#yawko na bukas ko na ulit are uupdate hehehhe

  
# CYLINDIRCAL MANIPULATOR OF COMPANY 8

###

<img align="left" height="220" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/eefd97a7-eb06-4151-9470-64c19e1b5ac4"/> 
<img align="right" height="220" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/eefd97a7-eb06-4151-9470-64c19e1b5ac4"/> 
</p>

.

###

<img align="left" height="60" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/58e6181e-cbbb-49a3-b613-3f018c737fec"/> 
<img align="right" height="60" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/58e6181e-cbbb-49a3-b613-3f018c737fec"> 
<p align="center">
  <img width="900" height="200" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/0b935dce-8c79-4c9d-8128-62c4c9e5f19a">
</p>

###

###

###

###

<img align="left" height="200" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/afc8f8c8-6810-4517-9328-85884a332aa1"/> 
<img align="right" height="200" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/afc8f8c8-6810-4517-9328-85884a332aa1"> 
<p align="center">
  <img  height="500" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/6fe6c94c-29ce-4b22-aa5f-41a7dd256bed">
</p>

###

<img align="left" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
<img align="right" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
</p>

###
.
###
###
###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚ Introduction 

 ###
 
> A cylindrical manipulator is an example of robotic device designed for three-dimensional object handling. It is also referred to as a cylindrical arm or robot. Just like the other robotic instruments, cylinder manipulators are designed to do the tasks that are not safe, hard labor, or difficult for workers to complete.

> Cylindrical manipulators can perform tasks with a high degree of precision and agility because of their unique shape and design. The manipulator's cylindrical shape and wide range of motion make it easy to rotate things and reach into small spaces. Depending on the intended use, the manipulator can be equipped with a several kinds of end-effectors, such as grippers, suction cups, and tool heads.

> Cylindrical manipulators are usually used in different industries, including manufacturing, automotive, and aerospace, as well as in research and development fields. They are often and usually used in assembly and disassembly tasks, as well as in handling and moving heavy or awkward objects in the field of industries.


###

###

<img align="left" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
<img align="right" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
</p>

###
.
###
###
###



 <h2 align="center"> ˚ ༘♡ ⋆｡˚ Abstract

 ###
> This read-me profile discusses the manipulator assigned to the said group, which is the cylindrical manipulator. The manipulator is an important tool commonly used in industries and manufacturing companies. This is part of the continuous advancement of research in its field. The main purpose of this task is to focus on a cylindrical manipulator, which involves solving degrees of freedom, assigning frames, obtaining the Denavit-Hartenberg parametric table, obtaining and solving the homogeneous transformation matrix, and solving the inverse kinematics using the graphical method. Aside from this, the task also deals with coding, specifically creating a calculator for both forward and inverse kinematics through Ubuntu Virtual Machine, Python, Peter Corke's Robotics Toolbox, and MATLAB. The cylindrical manipulator, along with its programmed GUI or Graphical User Interface calculator, will fulfill the requirements to solve forward and inverse kinematics easily, as well as verify the computations of different mathematical equations. This design is built to analyze and solve the problem to confirm the structure of the manipulator.

###

###

<img align="left" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
<img align="right" height="80" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ae9dacdb-6fc3-4208-8ce0-91f00b8d1af7"/> 
</p>

###
.
###
###
###


 <h2 align="center"> ˚ ༘♡ ⋆｡˚ SOLVING THE DEGREES OF FREEDOM OF A CYLINDRICAL MANIPULATOR

   
###
   
↳ DESCRIPTION ༉‧₊

###


<p align="center">
	
**`·..➭ HOW TO SOLVE THE DEGREES OF FREEDOM OF A CYLINDRICAL MANIPULATOR?**
	
</p>

###
ㅤㅤㅤ  
###

**‣ STEP-BY-STEP PROCESS**


###

**»** IDENTIFY THE NUMBER OF m JOINTS AND n RIGID MOVING LINKS OF THE MANIPULATOR.

**»** IDENTIFY THE NUMBER OF CONSTRAINTS OF THE JOINT PRESENT IN THE MANIPULATOR.


		FOR SPATIAL:					FOR PLANAR
		[6-Ci]							[3-Ci]

**»** COMPUTE THE MOBILITY OF THE MANIPULATOR WITH THE USE OF GRUBLER’S CRITERION.

		FOR SPATIAL:						FOR PLANAR:
		M= 6n-i=1m(6-Ci)						M= 3n-i=1m(3-Ci)


###

<p align="center">
  <img src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/c92ac953-ea46-4b92-87a2-c05e5c9b5d87">
</p>

###


**SOLUTION:**

	JOINTS (m) = 3						REVOLUTE (R) = ?
	LINKS (n) = 3							PRISMATIC (P) = ?

CYLINDRICAL MANIPULATOR IS A SPATIAL MANIPULATOR. THEREFORE, WE WILL USE THE FORMULA:

	M= 6n-i=1m(6-Ci)

CYLINDRICAL MANIPULATOR = RPP

	REVOLUTE = (6-Ci) = (6-1) = 5
	PRISMATIC 1 = (6-Ci) = (6-1) = 5
	PRISMATIC 2 =  (6-Ci) = (6-1) = 5

###

<p align="center">
  <img src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/1bbcd11a-2c60-419a-b508-e935fbb0faf2">
</p>

###

	M= 6n-i=1m(6-Ci)

	M = 6(3)-[(6-1)+(6-1)+(6-1)]
	M = 18 - (5+5+5)
	M =18-15
	M = 3
###


**THEREFORE, THIS IS AN UNDER ACTUATED SPATIAL MANIPULATOR WITH 3 DOF.**



###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT SOLVING THE THE DEGREES OF FREEDOM OF A CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###
<p align="center">
  <img width="600" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ee8ffc51-c634-4df1-99f2-58361922e94d
">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1VQinvBY4uOlH3hYz1ZLntOjnTrg3Q3Fj/view?usp=drive_link" target="_blank">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

###

![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###

 <h2 align="center">˚ ༘♡ ⋆｡˚ DH FRAME RULES OF CYLINDRICAL MANIPULATOR

###

↳ DESCRIPTION ༉‧₊

**`·..➭ HOW TO ASSIGN THE FRAMES OF A CYLINDRICAL MANIPULATOR?**

**‣ STEP-BY-STEP PROCESS**
 ㅤ

 ㅤ
 ㅤ
###

**» DENAVIT-HARTENBERG (DH) PRELIMINARY RULES**

 ###

**➥ RULE 1:** _DECIDE FIRST THE 3 VIEWS YOU WANT TO PROJECT ON YOUR ISOMETRIC DRAWING._

**➥ RULES 2:** _IDENTIFY THE CENTER OF THE FRAMES._

**➥ RULE 3:** _THEN DRAW YOUR COLOR CODED ARROWS BASED ON YOUR DECIDED 3 VIEWS._

**➥ RULES 4:** _REMEMBER TO MAKE THE ARROWS OF Z AND X AXES EASY TO SEE FOR FUTURE COMPUTATIONS._

ㅤ
ㅤ


###

**»DENAVIT-HARTENBERG (DH) FRAME RULES**

 ###

**➥ RULE 1:** _THE Z AXIS MUST BE THE AXIS OF ROTATION FOR A REVOLUTE/TWISTING, OR THE DIRECTION OF TRANSLATION FOR A PRISMATIC JOINT._

**➥ RULE 2:** _THE X AXIS MUST BE PERPENDICULAR BOTH TO ITS OWN Z AXIS AND THE Z AXIS OF THE FRAME BEFORE IT._

**➥ RULE 3:** _RULES FOR COMPLYING: EACH X AXIS MUST INTERSECT THE Z AXIS OF THE FRAME BEFORE IT._
_ROTATE THE AXIS UNTIL IT HITS THE OTHER_
_OR TRANSLATE THE AXIS UNTIL IT HITS THE OTHER_

**➥ RULE 4:** _ALL FRAMES MUST FOLLOW THE RIGHT HAND RULE_ 


###

<p align="center">
  <img length="100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/dbcf8610-0488-4048-a7c5-b19d15da8699">
</p>

###
<p align="center">
	
_FOR MORE EXPLANATION ABOUT DH FRAME RULES OF CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###

<p align="center">
  <img width="600" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/ee8ffc51-c634-4df1-99f2-58361922e94d">
</p>


<div align="center">
  <a href="https://drive.google.com/file/d/1VEsTEDOvEs3ZMVf_mdQ5YYfPlQSplw2u/view?usp=drive_link" target="_blank">
    <img height=100 src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>


###

![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚ DH PARAMETRIC TABLE OF CYLINDRICAL MANIPULATOR

###
↳ DESCRIPTION ༉‧₊

**`·..➭ HOW TO OBTAIN THE DENAVIT-HARTENBERG PARAMETRIC TABLE OF A 
CYLINDRICAL MANIPULATOR?**

**‣STEP-BY-STEP PROCESS**
ㅤ
ㅤ

ㅤ


**»DENAVIT-HARTENBERG NOTATION**

**➥STEP 1:** ASSIGN FRAMES ACCORDING TO THE 4 D-H FRAME RULES (ON TASK 2)

**➥STEP 2:** FILL OUT THE D-H PARAMETRIC TABLE (ON TASK 3)

**➥STEP 3:** PLUG THE TABLE INTO THE HOMOGENEOUS TRANSFORMATION MATRIX (ON TASK 4)

**➥STEP 4:** MULTIPLY THE MATRICES TOGETHER (ON TASK 4)


###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT DH FRAME RULES OF CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>

###
<p align="center">
  <img width="600" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/a862da91-833b-4276-acd7-e6ac5da338b0">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1WDlujtOCsjOI4wqjYOtqW2JSDW44mmZa/view?usp=drive_link" target="_blank">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

###
![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)
###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚ HOMOGENEOUS TRANSFORMATION MATRIX OF A CYLINDRCAL MANIPULATOR

###
↳ DESCRIPTION ༉‧₊

**`·..➭ HOW TO OBTAIN THE HOMOGENEOUS TRANSFORMATION MATRIX OF A 
CYLINDRICAL MANIPULATOR?**

**‣STEP-BY-STEP PROCESS**
ㅤ


ㅤ

<p align="center">	
»PARTS OF A HOMOGENEOUS TRANSFORMATION MATRIX
</p>


<p align="center">	
<img src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/9572909b-d2aa-42d3-b3f8-65d351477a6d">
</p>

<p align="center">	
»STANDARD FORMULA OF A HOMOGENEOUS TRANSFORMATION MATRIX
</p>
ㅤ
<p align="center">	
<img src= "https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/b6dd0db6-0984-496f-a84c-caf27baf1fff">
</p>
ㅤ
<p align="center">	
»DENAVIT-HARTENBERG PARAMETRIC TABLE OF A CYLINDRICAL MANIPULATOR
</p>
ㅤ
<p align="center">	
<img src= "https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/60236aab-9ca4-4dbe-9efc-8144c7d5abe6">
</p>
ㅤ

<p align="center">	
»SOLUTIONS FOR HOMOGENEOUS TRANSFORMATION MATRIX OF A CYLINDRICAL MANIPULATOR
</p>
ㅤ
<p align="center">	
<img src= "https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0689439e-b58f-48a2-a623-6acdeccd1863">
</p>
ㅤ




</p>

###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT DH FRAME RULES OF CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>

###
<p align="center">
  <img width="600" src="![pastel-academia-aesthetics-school-center pptx](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157549014/5f8354ef-8d86-47c2-83b8-683ecbf71be3)
">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1VJzvq5nUsGKtA6AyXkhUuszTYmCvZqyq/view?usp=sharing">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

###
![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###
  <h2 align="center"> ˚ ༘♡ ⋆｡˚ Solving Inverse Kinematics for Cylindrical Manipulator

###
↳ DESCRIPTION ༉‧₊

**`·..➭ HOW TO SOLVE THE INVERSE KINEMATIC SOLUTION USING GRAPHICAL METHOD OF A CYLINDRICAL MANIPULATOR**ㅤ

<p align="center">	
»FIGURE OF A CYLINDRICAL MANIPULATOR

</p>


<p align="center">	
<img src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/3361407e-ff45-4a55-a75c-76d31d5bb830">
</p>

ㅤ



**‣STEP-BY-STEP PROCESS**

<p align="center">	
➥ STEP 1: REDRAW THE GIVEN MANIPULATOR TO ITS TOP VIEW TO DERIVE THE SOLUTION OF THE INVERSE KINEMATICS USING PYTHAGOREAN THEOREM, SOHCAHTOA, AND LAW OF COSINES

</p>
ㅤ
<p align="center">	
<img src= "https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/2edc293c-3b14-4f94-be33-da822644f652">
</p>

ㅤ
<p align="center">	
➥STEP 2: REDRAW THE GIVEN MANIPULATOR TO ITS FRONT VIEW TO DERIVE THE SOLUTION OF THE INVERSE KINEMATICS

</p>
ㅤ
<p align="center">	
<img src= "https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/bb724aa0-c99e-4f5b-90ac-48bed2b3f061">
</p>
ㅤ

###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT DH FRAME RULES OF CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>

###
<p align="center">
  <img width="600" src="https://github.com/witchfrommercury/TESTING-FOR-PROFILE/assets/157728066/a862da91-833b-4276-acd7-e6ac5da338b0">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1U9jcroiBhVzGbekWbdQThGD9ZB5SY1Fr/view?usp=drive_link">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

###
![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚ CONCLUSION

 ###
 
<img align="left" height="300" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/41be1959-bab9-45d1-88b9-471b2281de14"/> 


>In this activity, I was able to review some topics from Robotics 1 that will help us to understand other topics in Robotics 2. It is important to learn the basics from solving the degrees of freedom up to solving the inverse kinematics before going to program your assigned manipulator. I also noticed how important the small details in programming, there are some things that cannot be taught at school but you need to discover it on your own to know its function and to widen our knowledge on programming using python. We also manage to build our own calculator for getting the forward and inverse kinematics of our cylindrical manipulator. We designed it based on our preference and  add other features to make it more lively and functional.

###
ㅤ
ㅤ

ㅤ

ㅤ
ㅤ
###
<img align="left" height="300" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/8f169b93-7631-4157-a627-ff9e14dc3a0c"/> 


>During this activity I've learned a lot of things about coding and the manipulators. We used the things we knew back then at Robotics 1 which we are applying right now at this laboratory activity. At first coding is kinda hard because the only course I've encounter which has coding is Programming. So I kinda  forgot the codes but eventually learned how to. I also learned how to code in Githu and use it. It is really fun and I did our readme and I enjoyed doing the readme. Even though at first it is hard to be familiarze in reaedme but later on coding became really easy work for me. So I've learned a lot valuable lesson and learnings from this laboratory activity. I've learned how to code manipulators also because I tried MatLab and Phyton on UBUNTU.

###

ㅤ
ㅤ

ㅤ

ㅤ
ㅤ



###
<img align="left" height="300" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/8b34d843-0e1b-4c72-909f-f4ffc5cad793"/> 

> All in all, I got a deeper understanding about the forward and inverse kinematics of some manipulators, especially the cylidrical variant. Also the programming part of the said kinematics in a python environment using different kinds of libraries to program the forward and inverse kinematics calculator and a graphical representation using the robotics toolbox. Using and learning GitHub with my groupmates was also fun as we can collaborate our works seamlessly and easily. Though there are certain problems like the buttons not working perfectly, robotics toolbox graphical representation does not look like what is expected, music does not play when the button is pressed, and many more, but it was such a fun experience.

###
ㅤ
ㅤ

ㅤ

ㅤ
ㅤ


###
<img align="left" height="300" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/ea11036c-4687-41c6-8dee-32c5d725efb2"/> 


>Learning subjects like Robotics 1 and Robotics 2 plays a crucial role in my life, especially as I pursue the Mechatronics engineering program. This serves as a means to develop my skills, both critical and analytical, as I am exposed to various topics, including different kinds of manipulators, degrees of freedom, assigning frames, creating D-H parametric tables, and solving inverse kinematics using graphical methods. Additionally, this activity enhances my programming skills, as we are instructed and guided by our professor, Engr. Mikko De Torres, in Python and Matlab. I have realized that building a robot or manipulator is not an easy task; it requires various steps, processes, and codes. However, this presents a valuable opportunity for me to create and explore other manipulators in the future. In addition, as the group's Project Quality, I learned how to connect with my groupmates and how to seek assistance when I had no idea what to do. This is not a one-man journey but rather a group effort; thus, what I learn is to be more open with the group members and prioritize the tasks that must be completed in order for the group to function smoothly and successfully. Overall, these characteristics and qualities are beneficial because I can apply them in the future when I begin working in the field.
